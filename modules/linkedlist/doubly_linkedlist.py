class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return
        
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        new_node.prev = curr


    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        
        if self.head:
            self.head.prev = new_node

        self.head = new_node

    def display(self):
        curr = self.head
        while curr:
            print(curr.data, end=" <-> ")
            curr = curr.next
        print("None")

    def reversed_display(self):
        if not self.head:
            print("The list is empty.")
            return
        
        curr = self.head
        while curr.next:
            curr = curr.next

        while curr:
            print(curr.data, end=" <-> ")
            curr = curr.prev
        print("None (Reversed)")

li  = DoublyLinkedList()

li.append(5)
li.append(7)
li.append(9)
li.prepend(10)
li.display()
li.reversed_display()
