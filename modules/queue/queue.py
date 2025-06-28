class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, *data):
        for x in data:
            self.queue.append(x)

    def enqueueleft(self, data):
        self.queue.insert(0, data) 

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return None

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        return None

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def display(self):
        return self.queue 

    def reset(self, *data):
        self.queue = list(data)


