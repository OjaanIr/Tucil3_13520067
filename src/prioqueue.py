class PriorityQueue:
    def __init__(self, filename):
        self.queue = []

    # Check emptiness
    def is_empty(self):
        return len(self.queue) == 0

    # Enqueue object to queue
    def enqueue(self, object):
        i = 0
        flag = False

        while (not flag and i < len(self.queue)):
            if (object.depth + object.root.calculate_misplaced_tiles() <= self.queue[i].depth + self.queue[i].root.calculate_misplaced_tiles()):
                flag = True
            else:
                i += 1
        
        self.queue.insert(i, object)

    # Dequeue queue 
    def dequeue(self):
        self.queue.pop(0)

    # Get value from front of queue
    def front(self):
        return self.queue[0]