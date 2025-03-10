#####################################################################
# Jan Berglund
#
# Exam
#
#####################################################################


import random

from src.gamefunctions import hit_it


class Item:
    """Representerar saker man kan plocka upp."""
    def __init__(self, name, value=20, symbol="?"):
        self.name = name
        self.value = value
        self.symbol = symbol

    def __str__(self):
        return self.symbol


# Used to randomize OG fruits and veggies for point pickups
pickups = [Item("carrot"), Item("apple"), Item("strawberry"), Item("cherry"),
           Item("watermelon"), Item("radish"), Item("cucumber"), Item("meatball")]


# Used to check if all OG items are picked up when
# crossing "E" (Exit) on the grid
def fill_exit_list():
    exit_list = []
    for item in range(0, len(pickups)):
        exit_list.append(pickups[item].name)
    return exit_list


# Used to randomize key(s) on the grid
keys = [Item("key", 0, "k")]

# Used to randomize chest(s) on the grid
chests = [Item("chest", 100, "c")]

# Used to randomize one trap on the grid
traps = [Item("trap", -10, "t")]

# Used to exit if all items in "pickups" has been harvested
exit_strategy = [Item("exit", 0, "E")]


# Used to collect the different items in lists into one place
list_of_all = pickups + keys + chests + traps + exit_strategy


# Used for fertile addons
pickups_fertile = [Item("mango", 25, "*"),
                   Item("lime", 25, "*"),
                   Item("orange", 25, "*")]


def randomize(grid):
    #Items to randomly place on the grid
    for item in list_of_all:
        while True:
            # slumpa en position tills vi hittar en som är ledig
            x = grid.get_random_x()
            y = grid.get_random_y()
            if grid.is_empty(x, y):
                grid.set(x, y, item)
                # abort while loop, continue with next iteration of for loop
                break


def fertile_generate(grid):
    while True:
        x = grid.get_random_x()
        y = grid.get_random_y()
        if grid.is_empty(x, y):
            new_fruit = random.choice(pickups_fertile)
            grid.set(x, y, new_fruit)
            print(f"New item has been added to x:{x}, y:{y}!")
            hit_it()
            break

