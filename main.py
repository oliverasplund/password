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



def settings(gen, ):
    try:
        with open('settings.json') as json_file:
            data = json.load(json_file)
        if gen:
            return [key for key, value in data['characters'].items() if value == 0], data['length']
        


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
            print(generate_password(*settings(True)))
        

        elif user_input == 2:
            while True:
                clear_screen
                print(f'0: Spara\n1: Bokstäver\n2: Siffror\n3: Tecken\n4: Längd\n5: xxxx-xxxx')
                user_input = user(0, 5)

                if user_input == 0:
                    break
                elif user_input == 1:
                    clear_screen
                    print(f'0: Spara\n1: Gemener\n2: Versaler\n\n')

        

app()