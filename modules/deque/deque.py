class Deque:
    """Custom Deque (Double-Ended Queue) using Python list."""

    def __init__(self):
        self.deque = []

    def append(self, *items):
        """Add item(s) to the right end."""
        for x in items:
            self.deque.append(x)

    def appendleft(self, *items):
        """Add item(s) to the left end."""
        for x in reversed(items):
            self.deque.insert(0, x)

    def pop(self):
        """Remove and return item from right end."""
        if not self.is_empty():
            return self.deque.pop()
        return None

    def popleft(self):
        """Remove and return item from left end."""
        if not self.is_empty():
            return self.deque.pop(0)
        return None

    def peek_left(self):
        """View the first element."""
        return self.deque[0] if not self.is_empty() else None

    def peek_right(self):
        """View the last element."""
        return self.deque[-1] if not self.is_empty() else None

    def is_empty(self):
        """Check if deque is empty."""
        return len(self.deque) == 0

    def size(self):
        """Return the number of items in deque."""
        return len(self.deque)

    def display(self):
        """Display the current deque."""
        return self.deque

    def reset(self, *items):
        """Replace deque with new items."""
        self.deque = list(items)
