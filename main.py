import random


def input_number():
    return input("Enter your number: ")


def input_choice():
    return input(str("Odd or Even?: "))


def random_number():
    return random.randint(1, 100)


def odd_or_even(x, y):
    num = x + y
    return num % 2 == 0


def moves():
    user_move = input_choice()

    player_number = int(input_number())
    bot_number = int(random_number())
    print("bot chose ", bot_number)
    results = (odd_or_even(player_number, bot_number))

    if user_move == "even" and results is True:
        print("You Won! The number is even!")
    elif user_move == "odd" and results is False:
        print("You Won! The number is odd!")
    else:
        print("You lost! The number is not", user_move)
    moves()


moves()
