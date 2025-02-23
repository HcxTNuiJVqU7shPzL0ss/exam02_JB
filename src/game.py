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
from .pickups import fertile_generate

player = Player(18, 6)    # Set player start pos in middle
score = 0                       # Starting score
inventory = []                  # Empty inventory at start

g = Grid()
g.set_player(player)
g.make_walls()
g.make_extra_walls()
pickups.randomize(g)


# List of acceptable commands, not including q, x, i
player_commands = ["a", "s", "d", "w"]

# List of exit commands
exit_commands = ["q", "x"]


command = "a"
in_ok = True

fertile_moves = 0


# Check if to allow values below 0 when walking on lava
neg_values = lava_negative()


# Loop until user/player inputs X or Q
while not command.casefold() in exit_commands:
    if in_ok:
        print_status(g, score)

    command = input("Use WASD to move, I for inventory, "
                    "Q/X to quit, only one char (Enter after input): \n")
    if len(command) != 1:
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
                if "key" in inventory:
                    score += maybe_item.value
                    str_print = (f"You found a {maybe_item.name}, +{maybe_item.value} points. "
                                 f"One key has been used and is now consumed.")
                    inventory.remove("key")
                else:
                    str_print = (f"You found a {maybe_item.name}, but you had no key.")
                    clear = False
            # Trap
            elif maybe_item.name == "trap":
                str_print = (f"Oh no, it is a {maybe_item.name}!")
                if score >= 10 or neg_values:
                    score += maybe_item.value
                else:
                    score = 0
                clear = False
            # Fruit / veggie
            elif maybe_item.value > 0:
                score += maybe_item.value
                str_print = f"You found a {maybe_item.name}, +{maybe_item.value} points."
            # Key
            else:
                str_print = f"You found a {maybe_item.name}!"
            print(str_print)
            #g.set(player.pos_x, player.pos_y, g.empty)
            if clear:
                g.clear(player.pos_x, player.pos_y)
                inventory.append(maybe_item.name)
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
            input("Press Enter to continue!")
        else:
            print("Inventory:")
            for item in inventory:
                print(item)
            input("Press Enter to continue!")


# This is where we end up when the while loop ends
print("Thank you for playing!")
