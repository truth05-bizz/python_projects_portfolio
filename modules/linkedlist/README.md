# 🔗 Linked List Module (Single Linked List)

This is a custom implementation of a **singly linked list** using Python classes. It's part of my journey to understand core data structures by building them from scratch.

## ✨ Features

- Append to the end
- Prepend to the beginning
- Insert after a given node
- Delete by value
- Delete by position
- Pop from left
- Get list size
- Display as a Python list

## 📁 File

- `linkedlist.py` — Contains the `Node` and `LinkedList` class definitions

## 📌 How to Use

```python
from modules.linkedlist.linkedlist import LinkedList

ll = LinkedList()
ll.append(10)
ll.append(20)
ll.prepend(5)
print(ll.display())  # Output: [5, 10, 20]


### 🔁 Circular Linked List

A circular singly linked list where the last node points back to the head. Includes:

- `append(data)`: Adds a new node to the list
- `display(limit=10)`: Prints the list safely (limited to avoid infinite loops)
- `prepend(data)`: Adds a new node to the beginning of the list
- `length()`: return the length of the list
- `remove(target_data)`: remove the target data from the list





