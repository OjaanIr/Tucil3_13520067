import copy
import os

def open_file(filename):
    d = os.getcwd()
    o = [os.path.join(d,o) for o in os.listdir(d) if os.path.isdir(os.path.join(d,o))]
    for item in o:
        if os.path.exists(item + '\\' + filename):
            file = item + '\\' + filename
    f = open(file, "r")
    return f

class Puzzle:
    # Constructor
    def __init__(self, filename):
        self.layout = []
        self.n = 0
        f = open_file(filename)
        for line in f:
            arr = line.split()
            self.layout.append(list(map(int, arr)))

        self.n = len(self.layout)

    # Find empty tile position
    def find_empty(self):
        for i in range(self.n):
            for j in range(self.n):
                if (self.layout[i][j] == 16):
                    return (i,j)

    # Move empty tile to certain position
    def move(self, direction):
        (r, c) = self.find_empty()
        moved_tile_puzzle = copy.deepcopy(self)

        # Move empty tile upward
        if (direction == "up"):
            if (r-1 >= 0):
                moved_tile_puzzle[r][c], moved_tile_puzzle[r-1][c] = moved_tile_puzzle[r-1][c], moved_tile_puzzle[r][c]
                return moved_tile_puzzle
            else:
                return None
        # Move empty tile downward
        elif (direction == "down"):
            if (r+1 <= self.n):
                moved_tile_puzzle[r][c], moved_tile_puzzle[r+1][c] = moved_tile_puzzle[r+1][c], moved_tile_puzzle[r][c]
                return moved_tile_puzzle
            else:
                return None
        # Move empty tile leftward
        elif (direction == "left"):
            if (c-1 >= 0):
                moved_tile_puzzle[r][c], moved_tile_puzzle[r][c-1] = moved_tile_puzzle[r][c-1], moved_tile_puzzle[r][c]
                return moved_tile_puzzle
            else:
                return None
        # Move empty tile rightward
        elif (direction == "right"):
            if (c+1 <= self.n):
                moved_tile_puzzle[r][c], moved_tile_puzzle[r][c+1] = moved_tile_puzzle[r][c+1], moved_tile_puzzle[r][c]
                return moved_tile_puzzle
            else:
                return None
        else:
            return None

    # Check whether puzzle is solvable or not
    def is_solvable(self):
        (r, c) = self.find_empty()

        flattened_layout = [num for arr in self.layout for num in arr]

        x = (r+c) % 2

        sum = 0
        for i in range(len(flattened_layout)):
            for j in range(i+1, len(flattened_layout)):
                if (flattened_layout[i] > flattened_layout[j]):
                    sum += 1
        
        return (sum + x) % 2 == 0

    # Print puzzle layout
    def print_puzzle(self):
        for row in self.layout:
            print("-----------------")
            print("|", end="")
            for num in row:
                print("%2s" % (num if num != 16 else " "), end=" ")
                print("|", end="")
            print()

    # g(i) function, calculate total misplaced tiles
    def calculate_misplaced_tiles(self):
        total = 0
        flattened_layout = [num for arr in self.layout for num in arr]

        for i in range(len(flattened_layout)):
            if (flattened_layout[i] != i+1):
                total += 1

        return total    