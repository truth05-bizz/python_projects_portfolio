class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop_left(self):
        if self.head is None:
            return None
        
        removed_data = self.head.data
        self.head = self.head.next
        return removed_data



    def insert_after(self, target_data, new_data):
        new_node = Node(new_data)
        curr = self.head
        while curr:
            if curr.data == target_data:
                new_node.next = curr.next
                curr.next = new_node
                return
            curr = curr.next


    def length(self):
        curr = self.head
        count = 0
        while curr:
            curr = curr.next
            count += 1
        return count
    
    def delete_by_value(self, target_data):
        if self.head is None:
            print("List is empty. Nothing to delete")
            return
        
        if self.head.data == target_data:
            self.head = self.head.next
            return
        
        curr = self.head
        prev = None

        while curr and curr.data != target_data:
            prev = curr
            curr = curr.next

        if curr is None:
            print(f"Value {target_data} not found in the list.")
            return
        
        prev.next = curr.next


    def delete_by_position(self, position):
        if self.head is None:
            print("List is empty")
            return

        if position == 0:
            self.head = self.head.next
            return
        
        curr = self.head
        prev = None
        count = 0

        while curr and count != position:
            prev = curr
            curr = curr.next
            count += 1

        if curr is None:
            print("Position out of range")
            return
        
        prev.next = curr.next
       

    def display(self):
        mylist = []
        curr = self.head
        while curr:
            mylist.append(curr.data)
            curr = curr.next
        return mylist

