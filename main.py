import random
from os import system, name
def clear_screen():
    system('cls') if name == 'nt' else system('clear')


characters = [("A", 0), ("B", 0), ("C", 0), ("D", 0), ("E", 0), ("F", 0), ("G", 0), ("H", 0), ("I", 0), 
              ("J", 0), ("K", 0), ("L", 0), ("M", 0), ("N", 0), ("O", 0), ("P", 0), ("Q", 0), ("R", 0), 
              ("S", 0), ("T", 0), ("U", 0), ("V", 0), ("W", 0), ("X", 0), ("Y", 0), ("Z", 0), 
              ("0", 0), ("1", 0), ("2", 0), ("3", 0), ("4", 0), ("5", 0), ("6", 0), ("7", 0), ("8", 0), ("9", 0),
              ("!", 0), ("?", 0), ("#", 0), ("%", 0), ("$", 0), ("&", 0), ("/", 0), ("+", 0), ("_", 0)]


def user(min, max):
    while True:
        try:
            user_input = int(input())

            if min <= user_input <= max:
                return user_input

        except ValueError:
            continue


def generate_password(allowed, length, letter_case=None):
    password = ""

    for i in range(length):
        password += random.choice(allowed)

    return password


def app():
    clear_screen()
    print(f'1: Generera lösenord\n2: Inställningar')

    user(1, 2)

    generate_password(allowed, length)