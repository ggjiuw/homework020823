import time
from time import sleep

user_animal = str(input("Enter the name of your favorite pet >> ")).strip('0`:;-=+_123456789,./ !@#$%^&*()[}{]')
user_animal = user_animal.lower()
animal_name = str(input('Enter your pet name >> ')).strip('0`:;-=+_123456789,./ !@#$%^&*()[}{]').title()

cat_emodji = '\U0001F431'
dog_emodji = '\U0001F436'
hamster_emodji = '\U0001F439'
fish_emodji = '\U0001F41F'
turtle_emodji = '\U0001F422'

can_pet_swim = False

if user_animal == 'turtle':
    can_pet_swim = True
    print(f'Turtles have strong shells{turtle_emodji}')
elif user_animal == 'fish':
    can_pet_swim = True
    print(f"Don't fry the fish{fish_emodji}")
elif user_animal == 'cat':
    print(f'Cats catch mice{cat_emodji}')
elif user_animal == 'dog':
    print(f'You are afraid when the dog barks, including if it {animal_name}{dog_emodji}')
elif user_animal == 'hamster':
    print(f'Hamsters are small{hamster_emodji}')
else:
    user_help = input("\nI don't know what kind of animal it is.\n type Help for a list of available pets >> ")
    if user_help.lower() == 'help':
        print('\nlist of pets:\nturtle , fish , dog , cat , hamster\n ')
        sleep(4)
        exit()
    else:
        exit()

if can_pet_swim is True:
    print('Your pet can swim, you need an aquarium')
