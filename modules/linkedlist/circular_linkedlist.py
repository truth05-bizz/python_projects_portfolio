class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return

        curr = self.head
        while curr.next != self.head:
            curr = curr.next

        curr.next = new_node
        new_node.next = self.head

    def display(self, limit=10):
        if not self.head:
            print("List is empty.")
            return

        curr = self.head
        count = 0
        while curr and count < limit:
            print(curr.data, end=" → ")
            curr = curr.next
            count += 1

        print("... (circular)")
