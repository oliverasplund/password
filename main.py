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



def settings():
    try:
        with open('settings.json') as json_file:
            data = json.load(json_file)
        return [key for key, value in data['characters'].items() if value == 0], data['length']
    except FileNotFoundError:
        print("Programmet hittar ej rätt fil")



def generate_password(allowed, length, letter_case=None):
    password = ""

    for _ in range(length):
        password += random.choice(allowed)

    return password


def app():
    clear_screen()
    print(f'1: Generera lösenord\n2: Inställningar')

    if user(1, 2) == 1:
        print(generate_password(*settings()))

    else:
        ...

app()