class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        newnode = Node(data)

        if self.rear is None:
            self.front = self.rear = newnode
            return

        self.rear.next = newnode
        self.rear = newnode

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None

        temp = self.front
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        return temp.data

    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return None

        return self.front.data

    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return

        temp = self.front
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()


# Driver Code
q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print("Queue:")
q.display()

print("Dequeued:", q.dequeue())

print("Front element:", q.peek())

print("Queue after dequeue:")
q.display()




class Queue:
    def __init__(self):
        self.items = []
        self.front = -1
        self.rear = -1

    def enqueue(self, item):
        self.items.append(item)
        self.rear += 1
        if self.front == -1:
            self.front = 0
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return -1
        item = self.items.pop(self.front)
        if self.is_empty():
            self.front = -1
            self.rear = -1
        return item

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
    
    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        for i in self.items:
            print(i, end=" ")
        print()
queue = Queue()

queue.dequeue()
queue.display()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.display()
queue.dequeue()
queue.display()