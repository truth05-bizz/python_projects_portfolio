import sys
import os

# Add 'modules' folder to the path
sys.path.append(os.path.abspath("modules"))

from modules.stack.stack import Stack
from modules.linkedlist.linkedlist import LinkedList

# Test LinkedList
ll = LinkedList()
ll.append(10)
ll.append(20)
print("LinkedList:", ll.display())

# Test for Stack
ly = Stack()
ly.push(12, 5, 8, 6)
ly.peek()
ly.size()
ly.pop()
ly.reset(5, 7, 9, 3, 1)
print("Stark:", ly.display())