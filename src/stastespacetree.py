class StateSpaceTree:
    # Constructor
    def __init__(self, node):
        self.node = node
        self.depth = 0
        self.parent = None

    # Add depth of state space tree
    def add_depth(self):
        self.depth += 1

    # Set parent of state space tree
    def set_parent(self, parent):
        self.parent = parent