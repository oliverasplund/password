import random
from os import system, name
import json

def clear_screen():
    system('cls') if name == 'nt' else system('clear')


def user(min, max):
    while True:
        user_input = input()

        if not user_input.isdigit():
            continue

        if min <= int(user_input) <= max:
            return int(user_input)





def settings(mode, length=None): # mode 1: gen, mode 2: retrieve
    try:
        with open('settings.json', 'r+') as file:
            data = json.load(file)

            if mode == "gen":
                return [key for key, value in data['characters'].items() if value == 0], data['length'], data['xxxx-xxxx']
            
            if mode == "retrieve":
                return [data['characters']['A'], data['characters']['b'], data['characters']['0'], data['characters']['='], data['xxxx-xxxx'], data['length']] # Versaler, gemener, siffror, tecken, xxxx-xxxx, längd
            
            elif mode == 1:
                for key in data['characters']:
                    if key.isupper():
                        data['characters'][key] = 1 if data['characters']['Z'] == 0 else 0
        
            elif mode == 2:
                for key in data['characters']:
                    if key.islower():
                        data['characters'][key] = 1 if data['characters']['z'] == 0 else 0

            elif mode == 3:
                for key in data['characters']:

                    if key.isdigit():
                        data['characters'][key] = 1 if data['characters']['9'] == 0 else 0


            elif mode == 4:
                for key in data['characters']:
                    if not key.isalpha() and not key.isdigit():   
                        data['characters'][key] = 1 if data['characters']['_'] == 0 else 0
                    
            
            elif mode == 5:
                data['xxxx-xxxx'] = 1 if data['xxxx-xxxx'] == 0 else 0

            elif mode == 6:
                data['length'] == length

            file.seek(0)
            json.dump(data, file, indent=4)



    except FileNotFoundError:
        print("Programmet hittar ej rätt fil")



def generate_password(allowed, length, xxxx):
    password = ""
    if xxxx == 0:
        while len(password) < length:
            for _ in range(4 if length-len(password) > 3 else length-len(password)):
                password += random.choice(allowed)
            if length != len(password):
                password += "-" 

    else:
        for _ in range(length):
            password += random.choice(allowed)

    return password


def app():
    while True:
        clear_screen()
        print(f'0: Avsluta\n1: Generera lösenord\n2: Inställningar')

        user_input = user(0,2)
        if user_input == 0:
            break

        elif user_input == 1:
            clear_screen()
            print(generate_password(*settings("gen")))
            break
        

        elif user_input == 2:
            while True:

                retrieve_settings = settings("retrieve")
                clear_screen()
                print(f'0: Spara\n1: Versaler\t{"på" if retrieve_settings[0]==0 else "av"}\n2: Gemener\t{"på" if retrieve_settings[1]==0 else "av"}\n3: Siffror\t{"på" if retrieve_settings[2]==0 else "av"}\n4: Tecken\t{"på" if retrieve_settings[3]==0 else "av"}\n5: xxxx-xxxx\t{"på" if retrieve_settings[4]==0 else "av"}\n6: Längd\t{retrieve_settings[5]}')
                user_input = user(0, 6)

                if user_input == 0:
                    break
                elif user_input == 6:
                    ...
                else:
                    settings(user_input)
                    

        

app()