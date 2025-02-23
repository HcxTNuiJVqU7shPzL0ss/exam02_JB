#####################################################################
# Jan Berglund
#
# Exam
#
#####################################################################


class Item:
    """Representerar saker man kan plocka upp."""
    def __init__(self, name, value=20, symbol="?"):
        self.name = name
        self.value = value
        self.symbol = symbol

    def __str__(self):
        return self.symbol


# Used to randomize fruits and veggies for point pickups
pickups = [Item("carrot"), Item("apple"), Item("strawberry"), Item("cherry"),
           Item("watermelon"), Item("radish"), Item("cucumber"), Item("meatball")]

# Used to randomize key(s) on the grid
keys = [Item("key", 0, "k")]

# Used to randomize chest(s) on the grid
chests = [Item("chest", 100, "c")]

# Used to randomize one trap on the grid
traps = [Item("trap", -10, "t")]

# Used to collect the different items in lists into one place
list_of_all = pickups + keys + chests + traps


def randomize(grid):
    #Items to randomly place on the grid
    for item in list_of_all:
        while True:
            # slumpa en position tills vi hittar en som är ledig
            x = grid.get_random_x()
            y = grid.get_random_y()
            if grid.is_empty(x, y):
                grid.set(x, y, item)
                break  # avbryt while-loopen, fortsätt med nästa varv i for-loopen
    # # Pickup "points" items
    # for item in pickups:
    #     while True:
    #         # slumpa en position tills vi hittar en som är ledig
    #         x = grid.get_random_x()
    #         y = grid.get_random_y()
    #         if grid.is_empty(x, y):
    #             grid.set(x, y, item)
    #             break  # avbryt while-loopen, fortsätt med nästa varv i for-loopen
    # # Pickup "keys)"
    # for content in keys:
    #     while True:
    #         x = grid.get_random_x()
    #         y = grid.get_random_y()
    #         if grid.is_empty(x, y):
    #             grid.set(x, y, content)
    #             break  # abort while loop, continue next in for loop
    # # Pickup "chests)"
    # for content in chests:
    #     while True:
    #         x = grid.get_random_x()
    #         y = grid.get_random_y()
    #         if grid.is_empty(x, y):
    #             grid.set(x, y, content)
    #             break  # abort while loop, continue next in for loop
