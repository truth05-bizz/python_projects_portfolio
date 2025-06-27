class Stack:
    def __init__(self):
        self.stack = []

    def push(self, *item):
        for x in item:
            self.stack.append(x)

    def is_empty(self):
        return len(self.stack) == 0
        
    def pop(self):
        if self.stack:
            return self.stack.pop()
        return None
    
    def size(self):
        return len(self.stack)

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None
    
    def display(self):
        return self.stack
    
    def reset(self, *item):
        new_list = list(item)
        self.stack = new_list
