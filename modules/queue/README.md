# Queue Module 🟦

This module contains a custom Queue class built with Python lists.

## Features

- `enqueue(data)` – Add data to end of queue
- `enqueueleft(data)` – Add data to the front
- `dequeue()` – Remove from front
- `peek()` – View front element
- `is_empty()` – Check if empty
- `size()` – Get current size
- `display()` – Show all elements
- `reset(data)` – Reset queue with new items

## Example

```python
from modules.queue.queue import Queue

q = Queue()
q.enqueue(10, 20)
q.enqueueleft(5)
q.dequeue()        # Returns 5
print(q.display()) # Output: [10, 20]
