class StateSpaceTree:
    # Constructor
    def __init__(self, start_state):
        self.root = start_state
        self.depth = 0
        self.parent = None