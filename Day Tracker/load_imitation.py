from os import system
import time
import languages

def imitating_load(status):
    if status == '_on':
        system('cls')
        loading = languages.lang_load[open('Settings.txt').readlines()[0][0:2]] + ' []'
        print(loading)
        for load in range(10):
            time.sleep(0.1)
            system('cls')
            loading += '[-]'
            print(loading)
        system('cls')
        print(loading + '[]')
        time.sleep(0.5)