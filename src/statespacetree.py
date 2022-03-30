class StateSpaceTree:
    node_generated = 0

    # Constructor
    def __init__(self, node):
        self.node = node
        self.depth = 0
        self.parent = None
        self.__class__.node_generated += 1

    # Add depth of state space tree
    def add_depth(self, parent):
        self.depth = parent.depth + 1   

    # Set parent of state space tree
    def set_parent(self, parent):
        self.parent = parent