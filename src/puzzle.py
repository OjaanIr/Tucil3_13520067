import copy
import random

class Puzzle:
    # Constructor
    def __init__(self, filename=""):
        self.layout = []
        self.n = 0

        # Input layout puzzle from file
        if (filename != ""):
            try:
                f = open(filename, "r")
                for line in f:
                    arr = line.split()
                    self.layout.append(list(map(int, arr)))
            except FileNotFoundError:
                print("File not found!")
        # Random generated puzzle layout
        else:
            array_of_num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
            for i in range(4):
                arr = []
                for j in range(4):
                    temp = random.choice(array_of_num)
                    array_of_num.remove(temp)
                    arr.append(temp)
                self.layout.append(arr)

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
                moved_tile_puzzle.layout[r][c], moved_tile_puzzle.layout[r-1][c] = moved_tile_puzzle.layout[r-1][c], moved_tile_puzzle.layout[r][c]
                return moved_tile_puzzle
            else:
                return None
        # Move empty tile downward
        elif (direction == "down"):
            if (r+1 < self.n):
                moved_tile_puzzle.layout[r][c], moved_tile_puzzle.layout[r+1][c] = moved_tile_puzzle.layout[r+1][c], moved_tile_puzzle.layout[r][c]
                return moved_tile_puzzle
            else:
                return None
        # Move empty tile leftward
        elif (direction == "left"):
            if (c-1 >= 0):
                moved_tile_puzzle.layout[r][c], moved_tile_puzzle.layout[r][c-1] = moved_tile_puzzle.layout[r][c-1], moved_tile_puzzle.layout[r][c]
                return moved_tile_puzzle
            else:
                return None
        # Move empty tile rightward
        elif (direction == "right"):
            if (c+1 < self.n):
                moved_tile_puzzle.layout[r][c], moved_tile_puzzle.layout[r][c+1] = moved_tile_puzzle.layout[r][c+1], moved_tile_puzzle.layout[r][c]
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
        print(f"X = {x}")

        sum = 0
        for i in range(len(flattened_layout)):
            inversion = 0
            for j in range(i+1, len(flattened_layout)):
                if (flattened_layout[i] > flattened_layout[j]):
                    inversion += 1
            sum += inversion
            print(f"Inversion ({i}) = {inversion}")

        is_even = (sum + x) % 2 == 0
        print(f"Total inversions = {sum}")
        print(f"Total inversions + X = {sum + x} %s" % ("(even)" if (is_even) else "(odd)"))
        
        return is_even

    # Print puzzle layout
    def print_puzzle(self):
        for row in self.layout:
            print("-----------------")
            print("|", end="")
            for num in row:
                print("%2s" % (num if num != 16 else " "), end=" ")
                print("|", end="")
            print()
        print("-----------------")

    # Calculate total misplaced tiles
    def calculate_misplaced_tiles(self):
        total = 0
        flattened_layout = [num for arr in self.layout for num in arr]

        for i in range(len(flattened_layout)):
            if (flattened_layout[i] != i+1):
                total += 1

        return total   

    # Check if the puzzle is solved
    def is_solved(self):
        flattened_layout = [num for arr in self.layout for num in arr]

        for i in range(len(flattened_layout)):
            if (flattened_layout[i] != i+1):
                return False
        
        return True