# Deque Module 🔁

A double-ended queue (deque) implementation using Python list. You can add or remove items from both ends.

## Features

- `append()` – Add to right end
- `appendleft()` – Add to left end
- `pop()` – Remove from right
- `popleft()` – Remove from left
- `peek_left()` – View first element
- `peek_right()` – View last element
- `is_empty()` – Check if empty
- `size()` – Length of deque
- `reset()` – Replace all items
- `display()` – View current state

## Example

```python
from modules.deque.deque import Deque

d = Deque()
d.append(1, 2)
d.appendleft(0)
print(d.display())  # [0, 1, 2]
