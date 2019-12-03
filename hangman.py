import random
import sys
from os import system, name


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def pick_capital():
    capitals = ["BUDAPEST", "WIEN", "BERLIN"]
    city = random.choice(capitals)
    print(city)
    return city
    '''
    Picks a random European capital

    Returns:
    str: The name of European capital
    '''
    pass


def get_hashed(word):

    letters = len(word)
    x = 0
    for x in range(letters):
        print("_", end =" ")

    print(" ")
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
    HP = 10
    sol = [""]
    RC=len(password)
    clear()
    LC=list(password)
    while HP > 0:
        
        for i in range(RC):
            sol.append("_")
            if LC[i] == letter:
                sol[i] = LC[i]
            else:
                HP=HP-1
            print(sol[i], end =" ")
        if HP > 0:
            get_input()
            print(HP)
        else:
            print(HP)
            break
        print("\n")
    

    
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


def is_win(life, points, leng):
    pass

#def is_loose(life_points):

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
    return guess.upper()
    '''
    Reads a user input until it contains only letter

    Returns:
    str: The validated input
    '''
    pass


def main():
    info = pick_capital()
    infolen = len(info)
    uncover(get_hashed(info), info, get_input())
    pass


if __name__ == '__main__':
    main()
