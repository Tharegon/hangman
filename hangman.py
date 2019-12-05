import random
import sys
from os import system, name


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def pick_capital():
    capitals = ["BUDAPEST", "WIEN", "LONDON"]
    city = random.choice(capitals)
    city = list(city)
    return city
    '''
    Picks a random European capital

    Returns:
    str: The name of European capital
    '''
    pass


def get_hashed(word):

    letters = len(word)
    hashed_city = []
    for x in range(letters):
        hashed_city.append("_")
    
    return hashed_city

    '''
    Generates a password based on the word with dashes instead of letters
    Keeps whitespaces undashed.

    Args:
    str: The word to hash

    Returns:s
    str: The hashed password
    '''
    pass

def uncover(hashed_password, password, letter):
    hash_len = len(hashed_password)
    for i in range(hash_len):
        if letter == password[i]:
            hashed_password[i] = password[i]
    return hashed_password

    '''
    Uncovers all occurences of the given letter in the hashed password based on the password

    Args:
    str: The hashed password
    str: The password
    str: The letter to uncover

    Returns:
    str: The hashed password with uncovered letter
    '''
    pass


def update(used_letters, letter):
    
    '''
    Appends the letter to used_letters if it doesn't occur

    Args:
    list: The list of already used letters
    str: The letter to append

    Returns:
    list: The updated list of already used letters
    '''
    pass


def is_win(hashed_password, password):
    return hashed_password == password
    pass


def is_loose(life_points):

    '''
    Checks if life points is equal 0

    Args:
    int: The life life_points

    Returns:
    bool: True if life point is equal 0, False otherwise
    '''
    pass


def get_input():
    guess = input("Enter your guess: ")
    if guess.isalpha() is True:
        return guess.upper()
    else:
        print("Not a letter, please try again.")
        get_input
    '''
    Reads a user input until it contains only letter

    Returns:
    str: The validated input
    '''
    pass


def main():
    counter = 0
    citypass = pick_capital()
    hashed = get_hashed(citypass)
    print(get_hashed(citypass))
    
    while True:
        userinput = get_input()
        print(uncover(hashed, citypass, userinput))
        if is_win(citypass, hashed):
            break
    pass


if __name__ == '__main__':
    main()
