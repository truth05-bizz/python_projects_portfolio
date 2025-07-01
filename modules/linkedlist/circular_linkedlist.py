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

    def prepend(self, data):
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
            self.head = new_node

    def remove(self, target_data):
        if not self.head:
            print("List is empty.")
            return
        
        curr = self.head
        prev = None

        # Handle head removal
        if curr.data == target_data:
            # Only one node
            if curr.next == self.head:
                self.head = None
                return
            
            # Find last node to fix the Link
            while curr.next != self.head:
                curr = curr.next

            curr.next = self.head.next
            self.head = self.head.next
            return
        
        # Handle non-head removal
        prev = self.head
        curr = self.head.next
        while curr != self.head:
            if curr.data == target_data:
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next

        print(f"{target_data} not found in the list.")


    def length(self):
        if not self.head:
            return 0
        
        count = 1
        curr = self.head
        while curr.next != self.head:
            curr = curr.next
            count += 1
        return count
    
    

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
