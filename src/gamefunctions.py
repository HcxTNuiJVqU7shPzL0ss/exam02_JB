#####################################################################
# Jan Berglund
#
# Exam
#
#####################################################################


import random


from .grid import Grid
from .player import Player


# Start info to the user
def start_info(first):
    if first:
        print("\nWelcome to the exciting game of Exam!\n")
        hit_it()
    print("\nValid commands are:\n* w to move up\n"
          "* a to move left\n* s to move down\n* d to move right\n"
          "* q or x to exit the game\n* i for inventory\n"
          "* h to display this info again\n")
    hit_it()
    if first:
        neg_values = lava_negative()
        return neg_values


# Function to print the status (score) and game board
def print_status(game_grid, score):
    """Display the board grid and number of points"""
    print("--------------------------------------")
    print(f"You have {score} points.")
    print(game_grid)


# Function to check which valid "move" command was entered
# Also handles if allowed to move, or a wall is in the way
def handle_commands(command_in, player_in, g_in):
    x = 0
    y = 0

    if command_in == "d":  # move right
        x = 1
    elif command_in == "a":
        x = -1
    elif command_in == "w":
        y = -1
    elif command_in == "s":
        y = 1

    # Check if allowed to move, or a wall
    if not player_in.can_move(x, y, g_in):
        x = 0
        y = 0

    return [x, y]


# Check if "The Floor is Lava!" allows values less than 0, or not
def lava_negative():
    while True:
        neg_check = input("\nDo you want to allow negative values (y)?\n")
        if len(neg_check) > 1:
            print("Please use only one character!")
            continue
        else:
            neg_check = neg_check.casefold()[:1]
            if neg_check == "y":
                return True
            else:
                return False


# Function to force user to hit enter to continue
def hit_it():
    input("Press Enter to continue!")


def check_secret(command):
    if command == "42":
        print("You found it!")
        return True
    else:
        return False
