class StateSpaceTree:
    node_generated = 0

    # Constructor
    def __init__(self, node):
        self.node = node
        self.depth = 0
        self.parent = None
        self.move_direction = ""
        if (node != None):
            self.__class__.node_generated += 1

    # Add depth of state space tree
    def add_depth(self, parent):
        self.depth = parent.depth + 1   

    # Set parent of state space tree
    def set_parent(self, parent):
        self.parent = parent

    # Set move direction
    def set_move_direction(self, direction):
        self.move_direction = direction

    # Return possible move from current state to next state
    def possible_move(self):
        if (self.move_direction == "up"):
            return ["up", "left", "right"]
        elif (self.move_direction == "down"):
            return ["down", "left", "right"]
        elif (self.move_direction == "left"):
            return ["up", "down", "left"]
        elif (self.move_direction == "right"):
            return ["up", "down", "right"]
        else:
            return ["up", "down", "left", "right"]

    # Get solution from searching process
    def get_solution(self):
        solution = []

        final_state = self
        prev_state = self.parent

        while (prev_state != None):
            solution.insert(0, final_state)
            final_state = prev_state
            prev_state = final_state.parent

        return solution

    # Show solution
    def show_solution(self):
        solution = self.get_solution()
        
        for state in solution:
            print(f'Move {state.move_direction}')
            state.node.print_puzzle()
            print()