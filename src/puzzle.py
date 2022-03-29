import copy

class Puzzle:
    '''
    Kelas Puzzle
    '''
    # Class attribute
    layout = []
    n = 0

    #Constructor
    def __init__(self, path):
        f = open(path, "r")
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


# array = []
# f = open("test.txt", "r")
# for line in f:
#     arr = line.split()
#     array.append(list(map(int, arr)))
#     print(array)
# new = [num for arr in array for num in arr]
# print(new)
# print()
# for row in array:
#     print("-----------------")
#     print("|", end="")
#     for num in row:
#         print("%2s" % (num if num != 16 else " "), end=" ")
#         print("|", end="")
#     print()
# for i in range(len(array)):
#             for j in range(len(array)):
#                 if (array[i][j] == 16):
#                     print(f"({i}, {j})")