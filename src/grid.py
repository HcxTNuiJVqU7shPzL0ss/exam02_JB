#####################################################################
# Jan Berglund
#
# Exam
#
#####################################################################


import random

class Grid:
    """"Represents the game board grid setup.
    It is OK to change the symbols for different squares."""
    width = 37
    height = 13
    empty = "."  # Symbol for an empty square
    wall = "■"   # Symbol for a (normally impenetrable) wall

    def __init__(self):
        """Create an object of the class Grid"""
        # Spelplanen lagras i en lista av listor.
        # Vi använder "list comprehension" för att sätta tecknet för "empty"
        # på varje plats på spelplanen.
        self.data = [[self.empty for y in range(self.width)] for z in range(
            self.height)]


    def get(self, x, y):
        """Hämta det som finns på en viss position"""
        return self.data[y][x]

    def set(self, x, y, value):
        """Ändra vad som finns på en viss position"""
        self.data[y][x] = value

    def set_player(self, player):
        self.player = player

    def clear(self, x, y):
        """Ta bort item från position"""
        self.set(x, y, self.empty)

    def __str__(self):
        """Gör så att vi kan skriva ut spelplanen med print(grid)"""
        xs = ""
        for y in range(len(self.data)):
            row = self.data[y]
            for x in range(len(row)):
                if x == self.player.pos_x and y == self.player.pos_y:
                    xs += "@"
                else:
                    xs += str(row[x])
            xs += "\n"
        return xs


    def make_walls(self):
        """Skapa väggar runt hela spelplanen"""
        for i in range(self.height):
            self.set(0, i, self.wall)
            self.set(self.width - 1, i, self.wall)

        for j in range(1, self.width - 1):
            self.set(j, 0, self.wall)
            self.set(j, self.height - 1, self.wall)


    def make_extra_walls(self):
        """Create extra walls"""
        y_coord_start = [3, 5] # Start at x = 3, y = 5
        y_length = 4 # Make 4 wall segments
        for n in range(y_length):
            self.set(y_coord_start[0], y_coord_start[1] + n, self.wall)

        x_coord_start = [17, 4]  # Start at x = 17, y = 4
        x_length = 6  # Make 6 wall segments
        for m in range(x_length):
            self.set(x_coord_start[0] + m, x_coord_start[1], self.wall)


    # Används i filen pickups.py
    def get_random_x(self):
        """Slumpa en x-position på spelplanen"""
        return random.randint(0, self.width-1)

    def get_random_y(self):
        """Slumpa en y-position på spelplanen"""
        return random.randint(0, self.height-1)


    def is_empty(self, x, y):
        """Returnerar True om det inte finns något på aktuell ruta"""
        return self.get(x, y) == self.empty

