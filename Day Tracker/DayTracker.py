import constant_settings
import languages
import settings
import my_plans

while True:
    cs = constant_settings.use_constant_settings()
    try:
        menu_select = int(input('\n' + languages.lang_select[cs['lang']] + '\n\n'
        '1. ' + languages.lang_my_plans[cs['lang']] + '\n\n'
        '2. ' + languages.lang_setting[cs['lang']] + '\n\n'
        '3. ' + languages.lang_quit[cs['lang']] + '\n\n'))
    except:
        continue
    if menu_select == 1:
        my_plans.open_my_plans()
    if menu_select == 2:
        settings.change_settings()
    if menu_select == 3:
        break