import argparse 
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
        check = input("Using external file or not? (y/n): ")
    if (check == "y"):
        filename = input("Input filename (.txt): ")
        tree = StateSpaceTree(Puzzle("../test/" + filename))
    elif (check == "n"):
        tree = StateSpaceTree(Puzzle())
    
# tree.node.print_puzzle()