class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        newnode = Node(data)

        if self.head is None:
            self.head = newnode
            return

        newnode.next = self.head
        self.head = newnode

    def insert_at_end(self, data):
        newnode = Node(data)

        if self.head is None:
            self.head = newnode
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next

        temp.next = newnode

    def insert_at_index(self, data, index):
        newnode = Node(data)

        if index == 0:
            newnode.next = self.head
            self.head = newnode
            return

        temp = self.head

        for i in range(index - 1):
            if temp is None:
                print("Index out of range")
                return
            temp = temp.next

        if temp is None:
            print("Index out of range")
            return

        newnode.next = temp.next
        temp.next = newnode

    def traverse(self):
        temp = self.head

        if temp is None:
            print("Linked List is empty")
            return

        while temp is not None:
            print(f"{temp.data} -> ", end="")
            temp = temp.next

        print("None")


# Driver Code
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

ll.insert_at_index(999, 6)
ll.traverse()