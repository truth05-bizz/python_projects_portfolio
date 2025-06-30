class Queue:
    """A basic implementation of a Queue using Python list (FIFO)."""

    def __init__(self):
        """Initialize an empty queue."""
        self.queue = []

    def enqueue(self, *data):
        """Add one or more elements to the end of the queue."""
        for x in data:
            self.queue.append(x)

    def enqueueleft(self, *data):
        """Add one or more elements to the front of the queue."""
        for x in reversed(data):
            self.queue.insert(0, x)

    def dequeue(self):
        """Remove and return the front element of the queue."""
        if self.queue:
            return self.queue.pop(0)
        return None

    def peek(self):
        """Return the front element without removing it."""
        if not self.is_empty():
            return self.queue[0]
        return None

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.queue) == 0

    def size(self):
        """Return the size of the queue."""
        return len(self.queue)

    def display(self):
        """Display the current queue."""
        return self.queue

    def reset(self, *data):
        """Replace current queue with new data."""
        self.queue = list(data)
