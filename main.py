import random
from os import system, name
import json

def clear_screen():
    system('cls') if name == 'nt' else system('clear')


def user(min, max):
    while True:
        try:
            user_input = int(input())

            if min <= user_input <= max:
                return user_input

        except ValueError:
            continue



def settings(mode, length=None): # mode 1: gen, mode 2: retrieve
    try:
        with open('settings.json') as file:
            data = json.load(file)

            if mode == 1:
                return [key for key, value in data['characters'].items() if value == 0], data['length']
            
            if mode == 2:
                return [data['characters']['A'], data['characters']['b'], data['characters']['0'], data['characters']['='], data['xxxx-xxxx'], data['length']] # Versaler, gemener, siffror, tecken, xxxx-xxxx, längd
            
            if mode == "change_upper":
                for key in data['characters']:
                    if key.isupper():
                        data['characters'][key] = 1 if data['characters']['A'] == 0 else 0
        
            if mode == "change_lower":
                for key in data['charaters']:
                    if key.islower():
                        data['characters'][key] = 1 if data['characters']['a'] == 0 else 0

            if mode == "change_integers":
                for key in data['charaters']:
                    if isinstance(key, int):
                        data['characters'][key] = 1 if data['characters']['0'] == 0 else 0

            if mode == "change_special":
                for key in data['characters']:
                    if not key.isupper() and not key.islower() and not isinstance(key, int):
                        data['characters'][key] = 1 if data['characters']['='] == 0 else 0
            
            if mode == "xxxx-xxxx":
                data['xxxx-xxxx'] == 1 if data['xxxx-xxxx'] == 0 else 0

            if mode == "length":
                data['length'] == length

            json.dump(data, file, indent=4)



    except FileNotFoundError:
        print("Programmet hittar ej rätt fil")



def generate_password(allowed, length):
    password = ""

    for _ in range(length):
        password += random.choice(allowed)

    return password


def app():
    clear_screen()
    while True:
        print(f'0: Avsluta\n1: Generera lösenord\n2: Inställningar')

        user_input = user(1,2)
        if user_input == 0:
            break

        elif user_input == 1:
            clear_screen
            print(generate_password(*settings(1)))
        

        elif user_input == 2:
            while True:

                retrieve_settings = settings(2)
                clear_screen
                print(f'0: Spara\n1: Versaler\t{"på" if retrieve_settings[0]==0 else "av"}\n2: Gemener\t{"på" if retrieve_settings[1]==0 else "av"}\n3: Siffror\t{"på" if retrieve_settings[2]==0 else "av"}\n4: Tecken\t{"på" if retrieve_settings[3]==0 else "av"}\n5: xxxx-xxxx\t{"på" if retrieve_settings[4]==0 else "av"}\n6: Längd\t{retrieve_settings[5]}')
                user_input = user(0, 5)

                if user_input == 0:
                    break
                elif user_input == 1:
                    settings(3)
                    

        

app()