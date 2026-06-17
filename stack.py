class Stack:
    def __init__(self):
        self.items = []
        self.top = -1
    def push(self,item):
        self.items.append(item)
        self.top += 1
    def pop(self):
        if self.top == -1:
            print("Stack is empty Cannot pop")
            return -1
        self.top -= 1
        return self.items.pop()
    def peek(self):
        if self.top == -1:
            print("Stack is empty Cannot peek")
            return -1
        return self.items[self.top]
    def isEmpty(self):
        if self.top == -1:
            return True
        return False
    def size(self):
        return self.top + 1
    def display(self):
        print("top item-> ",self.items[self.top])
        for i in range(self.top,-1,-1):
            print(f"|  {i} -> {self.items[i]}  |")
        print("--"*(self.top+1))
stack = Stack()
stack.pop()
stack.peek()
print(stack.isEmpty())
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.display()
stack.pop()
stack.display()
print(stack.size())