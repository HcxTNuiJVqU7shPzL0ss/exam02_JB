#####################################################################
# Jan Berglund
#
# Exam
#
#####################################################################


# from .grid import Grid
# from .player import Player
from . import pickups

from .gamefunctions import *
from .item_check import fun_chest, fun_trap
from .pickups import fertile_generate, fill_exit_list

player = Player(18, 6)    # Set player start pos in middle
score = 0                       # Starting score
inventory = []                  # Empty inventory at start

g = Grid()
g.set_player(player)
g.make_walls()
g.make_extra_walls()
pickups.randomize(g)


# List of acceptable commands, not including q, x, i, h
player_commands = ["a", "s", "d", "w"]

# List of exit commands
exit_commands = ["q", "x"]

# Default values
command = "a"
in_ok = True
all_done = False
fertile_moves = 0
check_pickups = fill_exit_list()


# Check if to allow values below 0 when walking on lava
# Also use this function to print start information to the
# user (help)
neg_values = start_info(True)


# Loop until user/player inputs X or Q
while not command.casefold() in exit_commands:
    str_print = ""
    if in_ok:
        print_status(g, score)

    command = input("Enter your command, only one char "
                    "(Enter after input): \n")
    # Secret stuff!!
    secret = check_secret(command)
    if secret:
        score += 42
        hit_it()
        continue
    elif len(command) != 1:
        print("Please only type one character")
        in_ok = False
        continue
    else:
        command = command.casefold()[:1]
        in_ok = True

    if command in player_commands:
        coords = handle_commands(command, player, g)

        maybe_item = g.get(player.pos_x + coords[0], player.pos_y + coords[1])
        player.move(coords[0], coords[1])
        clear = True
        all_done = False

        # After 25 moves, generate a new fruit/veggie
        if fertile_moves == 24:
            fertile_generate(g)
            fertile_moves = 0
        else:
            fertile_moves += 1

        if isinstance(maybe_item, pickups.Item):
            # we found something
            # Chest
            if maybe_item.name == "chest":
                result_chest = fun_chest(score, inventory, maybe_item)
                score = result_chest[0]
                str_print = result_chest[1]
                clear = result_chest[2]
            # Trap
            elif maybe_item.name == "trap":
                result_trap = fun_trap(score, maybe_item, neg_values)
                clear = False
                score = result_trap[0]
                str_print = result_trap[1]
            # Exit
            elif maybe_item.name == "exit":
                clear = False
                for check_item in check_pickups:
                    if check_item not in inventory:
                        str_print = "You have not yet picked up all OG items!"
                        all_done = False
                        break
                    else:
                        all_done = True
                        str_print = f"Way to go! You got score of: {score}!"
            # Fruit / veggie / etc.
            elif maybe_item.value > 0:
                score += maybe_item.value
                str_print = f"You found a {maybe_item.name}, +{maybe_item.value} points."
            # Key
            else:
                str_print = f"You found a {maybe_item.name}!"
            print(str_print)
            if clear:
                g.clear(player.pos_x, player.pos_y)
                inventory.append(maybe_item.name)

            hit_it()
        else:
            # Do not subtract points if attempting to move through a wall
            if coords[0] == 0 and coords[1] == 0:
                continue

            if score > 0:
                score -= 1
            else:
                if neg_values:
                    score -= 1

    # Handle inventory printout
    elif command == "i":
        if len(inventory) == 0:
            print("Inventory is empty!")
            hit_it()
        else:
            print("Inventory:")
            for item in inventory:
                print(item)
            hit_it()

    # Handle "help" printout
    elif command == "h":
        start_info(False)

    # Not recognized command
    elif command not in exit_commands:
        print("I do not know that command, please "
              "try again!")
        hit_it()

    if all_done:
        break


# This is where we end up when the while loop ends
# i.e. when the user selected either q or x
print("\nThank you for playing, come again soon!\n"
      "***** Please rate us 5 star! *****\n")
