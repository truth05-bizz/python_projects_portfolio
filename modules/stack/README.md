
---

## 🔹 `modules/stack/README.md`

```markdown
# 🥞 Stack Module (LIFO)

This project implements a **stack data structure** using Python lists, with full object-oriented design.

## ✨ Features

- Push one or more items
- Pop the last item
- Peek the top of the stack
- Reset the stack
- Check if empty
- Get size
- Display current stack

## 📁 File

- `stack.py` — Contains the `Stack` class

## 📌 How to Use

```python
from modules.stack.stack import Stack

s = Stack()
s.push(1, 2, 3)
print(s.pop())       # 3
print(s.peek())      # 2
print(s.display())   # [1, 2]
