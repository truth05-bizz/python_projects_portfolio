import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modules.linkedlist.linkedlist import LinkedList
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modules.stack.stack import Stack

# Test LinkedList
ll = LinkedList()
ll.append(10)
ll.append(20)
print("LinkedList:", ll.display())  # should show [10, 20]


# Test for Stack
li = Stack()
li.push(12, 5, 8, 6)
li.peek()
li.size()
li.pop()
li.reset(5, 7, 9, 3, 1)
print(li.display())
