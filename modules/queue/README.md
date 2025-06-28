# Queue Module 🟩

This is a simple implementation of a **Queue (FIFO)** in Python using lists.

## ✨ Features

- Enqueue multiple items at once
- Enqueue from the left (like a deque)
- Dequeue (removes from front)
- Peek at the front item
- Check if queue is empty
- Get size of queue
- Reset queue
- Display queue

## 🧪 Example

```python
from modules.queue.queue import Queue

q = Queue()
q.enqueue(1, 2, 3)
q.enqueueleft(0)
print(q.display())  # [0, 1, 2, 3]
print(q.dequeue())  # 0
print(q.peek())     # 1
print(q.size())     # 3
