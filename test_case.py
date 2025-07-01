import sys
import os

# Add 'modules' folder to the path
sys.path.append(os.path.abspath("modules"))

from modules.queue.queue import Queue
from modules.stack.stack import Stack
from modules.linkedlist.linkedlist import LinkedList
from modules.linkedlist.circular_linkedlist import CircularLinkedList

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

# Test Queue
q = Queue()
q.enqueue(1, 2, 3)
q.enqueueleft(0)
print("Queue after enqueues:", q.display())  # [0, 1, 2, 3]
print("Dequeued:", q.dequeue())             # 0
print("Peek:", q.peek())                    # 1
print("Size:", q.size())                    # 3
q.reset(10, 20)
print("After reset:", q.display())          # [10, 20]


# Circular_LinkedList

print("\n Circular Linked List Test")
cll = CircularLinkedList()
cll.append("A")
cll.append("B")
cll.append("C")
cll.display()