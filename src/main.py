import time
from puzzle import Puzzle
from statespacetree import StateSpaceTree
from prioqueue import PriorityQueue

# Check whether the user wants to run the program by using an external file or not
check = input("Do you use external file to run this program? (y/n): ")

if (check == "y"):
    filename = input("Enter filename (.txt): ")
    tree = StateSpaceTree(Puzzle("../test/" + filename))
elif (check == "n"):
    tree = StateSpaceTree(Puzzle())
else:
    while (check != "y" and check != "n"):
        print("Invalid input! Try again!")
        check = input("Do you use external file to run this program? (y/n): ")
    if (check == "y"):
        filename = input("Input filename (.txt): ")
        tree = StateSpaceTree(Puzzle("../test/" + filename))
    elif (check == "n"):
        tree = StateSpaceTree(Puzzle())
    
# Print the start state of puzzle
print()
print("This is the start state of puzzle")
tree.node.print_puzzle()
print()

# Check whether the puzzle is solvable or not
if (not tree.node.is_solvable()):
    print("This puzzle isn't solvable")
    exit()

print("This puzzle is solvable. Continuing program...")
print()

# Create priority queue for search needs
prioqueue = PriorityQueue()

# Enqueue start state of state space tree to priority queue
prioqueue.enqueue(tree)

# Start timer
start = time.process_time()

# Solving puzzle
final_state = prioqueue.solve()

# Stop timer
stop = time.process_time()

# Solution
final_state.show_solution()

# Time elapsed
time_elapsed = stop - start
print("Time elapsed = " + str(time_elapsed) + " s or " + str(time_elapsed * 10**3) + " ms")

# Total generated node
print("Total generated node =", StateSpaceTree.node_generated)