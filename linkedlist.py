class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_begining(self,data):
        # Step - 1 Create new node
        newnode = Node(data)
        # Check if the Linked List is empty
        if self.head is None:
            self.head = newnode
            return
        # Step - 2 Assign new node's next as head
        newnode.next = self.head
        # Step - 3 Now new node becomes the head
        self.head = newnode
    def insert_at_end(self,data):
        # Step - 1 Create new node
        newnode = Node(data)
        # Check if the Linked List is empty
        if self.head is None:
            self.head = newnode
            return
        # Step - 2 Traverse to the last node
        temp = self.head
        while temp.next != None:
            temp = temp.next
        # Step - 3 Insert the new node at the end
        temp.next = newnode
    def insert_at_index(self,data,index):
        # Step - 1 Create new node
        newnode = Node(data)
        # Check if the Linked List is empty
        if self.head is None:
            self.head = newnode
            return
        if index == 0:
            newnode.next = self.head
            self.head = newnode
            return
        # Step - 2 Traverse to the index-1 node
        temp = self.head
        for i in range(index-1):
            if temp is None:
                print("Index out of range")
                return
            temp = temp.next
        if temp is None:
                print("Index out of range")
                return
        # Step - 3 Insert the new node at the index
        newnode.next = temp.next
        temp.next = newnode
    def delete_at_begining(self):
        if self.head is None:
            print("Linked List is empty")
            return
        self.head = self.head.next
        return
    def delete_at_end(self):
        if self.head is None:
            print("Linked List is empty")
            return
        temp = self.head
        while temp.next.next != None:
            temp = temp.next
        temp.next = None
        return
    def delete_at_index(self,index):
        if self.head is None:
            print("Linked List is empty")
            return
        if index == 0:
            self.head = self.head.next
            return
        temp = self.head
        for i in range(index-1):
            if temp is None:
                print("Index out of range")
                return
            temp = temp.next
        if temp.next is None or temp is None:
                print("Index out of range")
                return
        temp.next = temp.next.next
        return
    def traverse(self):
        temp = self.head
        if temp == None:
            print("Linked List is empty")
            return
        while temp != None:
            print(f"{temp.data} -> ",end="")
            temp = temp.next
        print("None")

ll = LinkedList()
ll.traverse()
ll.insert_at_begining(10)
ll.traverse()
ll.insert_at_begining(20)
ll.insert_at_begining(30)
ll.insert_at_begining(40)
ll.insert_at_begining(50)
ll.traverse()
ll.insert_at_end(100)
ll.traverse()
ll.insert_at_index(999,7)
ll.traverse()
ll.delete_at_index(5)
ll.traverse()