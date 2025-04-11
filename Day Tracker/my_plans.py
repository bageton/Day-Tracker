from os import system
import datetime

import languages
import constant_settings

def open_my_plans():
    '''Open my plans menu
    
    
    Arguments: None
    
    Return: None
    
    
    '''
    while True:
        cs = constant_settings.use_constant_settings()
        try:    
            my_plans_select = int(input('\n' + languages.lang_select[cs['lang']] + '\n\n'
            '1. ' + languages.lang_create_plan[cs['lang']] + '\n\n'                            
            '2. ' + languages.lang_open_plan[cs['lang']] + '\n\n'
            '3. ' + languages.lang_edit_plan[cs['lang']] + '\n\n'
            '4. ' + languages.lang_back[cs['lang']] + '\n\n'))
        except:
            continue
        if my_plans_select == 1:
            creating_new_plan()
        if my_plans_select == 2:
            open_plan()                    
        if my_plans_select == 4:
            break

def creating_new_plan():
    while True:
        cs = constant_settings.use_constant_settings()
        try:    
            new_plan_select = int(input('\n' + languages.lang_select[cs['lang']] + '\n\n'
            '1. ' + languages.lang_create_today_plan[cs['lang']] + '\n\n'                            
            '2. ' + languages.lang_create_plan_for_other_days[cs['lang']] + '\n\n'
            '3. ' + languages.lang_back[cs['lang']] + '\n\n'))
        except:
            continue
        if new_plan_select == 1:
            creating_today_plan()
        if new_plan_select == 2:
            creating_plan_for_other_days()
        if new_plan_select == 3:
            break
        
def creating_plan_for_other_days():
    cs = constant_settings.use_constant_settings()
    year_select = input('\n' + languages.lang_year_select[cs['lang']] + ': ')
    month_select = input('\n' + languages.lang_month_select[cs['lang']] + ': ')
    day_select = input('\n' + languages.lang_day_select[cs['lang']] + ': ')
    template_plan = [f'{year_select}-{month_select}-{day_select}']
    while True:
        cs = constant_settings.use_constant_settings()
        try:
            today_plan_select = int(input('\n' + languages.lang_select[cs['lang']] + '\n\n'
            '1. ' + languages.lang_create_new_list[cs['lang']] + '\n\n'
            '2. ' + languages.lang_change_list[cs['lang']] + '\n\n'
            '3. ' + languages.lang_back[cs['lang']] + '\n\n'))
        except:
            continue
        if today_plan_select == 1:
            template_plan = creating_new_list(template_plan)
        if today_plan_select == 2:
            pass
        if today_plan_select == 3:
            break
    data = open('Plans/' + f'{year_select}-{month_select}-{day_select}' + '.txt', 'w').writelines('<b>'.join(template_plan))
    
def open_plan():
    cs = constant_settings.use_constant_settings()
    year_select = input('\n' + languages.lang_year_select[cs['lang']] + ': ')
    month_select = input('\n' + languages.lang_month_select[cs['lang']] + ': ')
    day_select = input('\n' + languages.lang_day_select[cs['lang']] + ': ')
    cs = constant_settings.use_constant_settings()
    data = open(f'Plans\{year_select}-{month_select}-{day_select}.txt').read().split('<b>')
    print(data[0] + '\n')
    for cl in range(1, len(data)):
        print(data[cl].split('<n>')[0] + ':')
        for ct in data[cl].split('<n>')[1].split('<t>'):
            print('- [] ' + ct)
    wait = input()
    
def creating_today_plan():
    template_plan = [str(datetime.date.today())]
    while True:
        cs = constant_settings.use_constant_settings()
        try:
            today_plan_select = int(input('\n' + languages.lang_select[cs['lang']] + '\n\n'
            '1. ' + languages.lang_create_new_list[cs['lang']] + '\n\n'
            '2. ' + languages.lang_change_list[cs['lang']] + '\n\n'
            '3. ' + languages.lang_back[cs['lang']] + '\n\n'))
        except:
            continue
        if today_plan_select == 1:
            template_plan = creating_new_list(template_plan)
        if today_plan_select == 2:
            pass
        if today_plan_select == 3:
            break
    data = open('Plans/' + str(datetime.date.today()) + '.txt', 'w').writelines('<b>'.join(template_plan))
    
def creating_new_list(template_plan):
    cs = constant_settings.use_constant_settings()
    new_list_name = input('\n' + languages.lang_new_list_name[cs['lang']] + ': ')
    new_list = []
    while True:
        cs = constant_settings.use_constant_settings()
        task_select = int(input('\n' + languages.lang_select[cs['lang']] + '\n\n'
            '1. ' + languages.lang_add_task[cs['lang']] + '\n\n'
            '2. ' + languages.lang_back[cs['lang']] + '\n\n'))
        if task_select == 1:
            cs = constant_settings.use_constant_settings()
            new_task = input('\n' + languages.lang_new_task[cs['lang']] + ': ')
            new_list.append(new_task)
        if task_select == 2:
            break
    template_plan.append(f'{new_list_name}<n>' + '<t>'.join(new_list))
    return template_plan