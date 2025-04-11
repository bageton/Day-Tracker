from os import system

import languages
import constant_settings

def change_settings():
    '''Open change settings menu
    
    
    Arguments: None
    
    
    Return: None
    
    
    '''
    while True:
        cs = constant_settings.use_constant_settings()
        try:    
            settings_select = int(input('\n' + languages.lang_select[cs['lang']] + '\n\n'
            '1. ' + languages.lang_change_language[cs['lang']] + '\n\n'
            '2. ' + languages.lang_change_date_format[cs['lang']] + '\n\n'
            '3. ' + languages.lang_switch_loading[cs['lang']] + '\n\n'
            '4. ' + languages.lang_back[cs['lang']] + '\n\n'))
        except:
            continue
        if settings_select == 1:
            try:
                new_language = change_language()
                if new_language:
                    data = open('Settings.txt').readlines()
                    data[0] = new_language + '\n'
                    open('Settings.txt', 'w').writelines(data)
            except:
                continue
        if settings_select == 2:
            try:
                new_date_format = change_date_format()
                if new_date_format:
                    data = open('Settings.txt').readlines()
                    data[2] = new_date_format + '\n'
                    open('Settings.txt', 'w').writelines(data)
            except:
                continue
        if settings_select == 3:
            new_loading_status = switch_loading(cs['status'])
            data = open('Settings.txt').readlines()
            data[1] = new_loading_status + '\n'
            open('Settings.txt', 'w').writelines(data)
        if settings_select == 4:
            break

def change_language():
    '''Open change language menu
    
    Arguments: None
    
    
    Return: str | bool
    
    
    '''
    while True:
        cs = constant_settings.use_constant_settings()
        try:    
            change_language_select = int(input('\n' + languages.lang_select[cs['lang']] + '\n\n'
            '1. ' + 'English' + '\n\n'
            '2. ' + 'Русский' + '\n\n'
            '3. ' + languages.lang_back[cs['lang']] + '\n\n'))
        except:
            continue
        if change_language_select == 1:
            return 'en'
        if change_language_select == 2:
            return 'ru'
        if change_language_select == 3:
            return False

def switch_loading(status):
    '''On / off loading
    
    Arguments: str
    
    
    Return: str
    
    
    '''
    if status == '_on':
        return 'off'
    if status == 'off':
        return '_on'

def change_date_format():
    while True:
        cs = constant_settings.use_constant_settings()
        try:    
            change_date_format = int(input('\n' + languages.lang_select[cs['lang']] + '\n\n'
            '1. ' + f'{languages.lang_day[cs['lang']]}-{languages.lang_month[cs['lang']]}-{languages.lang_year[cs['lang']]}' + '\n\n'
            '2. ' + f'{languages.lang_day[cs['lang']]}-{languages.lang_year[cs['lang']]}-{languages.lang_month[cs['lang']]}' + '\n\n'
            '3. ' + f'{languages.lang_month[cs['lang']]}-{languages.lang_day[cs['lang']]}-{languages.lang_year[cs['lang']]}' + '\n\n'
            '4. ' + f'{languages.lang_month[cs['lang']]}-{languages.lang_year[cs['lang']]}-{languages.lang_day[cs['lang']]}' + '\n\n'
            '5. ' + f'{languages.lang_year[cs['lang']]}-{languages.lang_day[cs['lang']]}-{languages.lang_month[cs['lang']]}' + '\n\n'
            '6. ' + f'{languages.lang_year[cs['lang']]}-{languages.lang_month[cs['lang']]}-{languages.lang_day[cs['lang']]}' + '\n\n'
            '7. ' + languages.lang_back[cs['lang']] + '\n\n'))
        except:
            continue
        if change_date_format == 1:
            return 'DD-MM-YYYY'
        if change_date_format == 2:
            return 'DD-YYYY-MM'
        if change_date_format == 3:
            return 'MM-DD-YYYY'
        if change_date_format == 4:
            return 'MM-YYYY-DD'
        if change_date_format == 5:
            return 'YYYY-DD-MM'
        if change_date_format == 6:
            return 'YYYY-MM-DD'
        if change_date_format == 7:
            return False