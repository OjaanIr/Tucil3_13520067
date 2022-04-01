from statespacetree import StateSpaceTree

class PriorityQueue:
    def __init__(self):
        self.queue = []

    # Check emptiness
    def is_empty(self):
        return len(self.queue) == 0

    # Enqueue object to queue
    def enqueue(self, object):
        i = 0
        flag = False

        while (not flag and i < len(self.queue)):
            if (object.depth + object.node.calculate_misplaced_tiles() <= self.queue[i].depth + self.queue[i].node.calculate_misplaced_tiles()):
                flag = True
            else:
                i += 1
        
        self.queue.insert(i, object)

    # Dequeue queue 
    def dequeue(self):
        current = self.queue[0]
        self.queue.pop(0)
        return current

    # Solving 15-puzzle
    def solve(self):
        # Solving puzzle
        while (not self.is_empty()):
            # Processing current state
            current_state = self.dequeue()

            # Check if the puzzle is solved
            if (current_state.node.is_solved()):
                final_state = current_state
                break
            
            # List of possible move directions
            possible_move_directions = current_state.possible_move()

            # Start searching for solution
            for direction in possible_move_directions:
                # Generate node
                new_node = StateSpaceTree(current_state.node.move(direction))
                new_node.add_depth(current_state)
                new_node.set_parent(current_state)
                new_node.set_move_direction(direction)

                # Check if move process is succeed
                if (new_node.node != None):
                    self.enqueue(new_node)
        
        return final_state