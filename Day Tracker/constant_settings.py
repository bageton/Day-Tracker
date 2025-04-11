from os import system

import load_imitation

def use_constant_settings():
    lang = open('Settings.txt').readlines()[0][0:2]
    status = open('Settings.txt').readlines()[1][0:3]
    date_format = open('Settings.txt').readlines()[2][0:10]
    load_imitation.imitating_load(status)
    system('cls')
    return {'lang': lang, 'status': status, 'date_format': date_format}