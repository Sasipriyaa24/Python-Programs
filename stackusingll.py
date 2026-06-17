class Node:
  def __init__(self,data):
    self.data=data
    self.next=None
class Stack:
  def __init__(self):
    self.top=None
  def push(self,data):
    newitem=Node(data)
    if self.top is None:
      self.top=newitem
      return
    newitem.next=self.top
    self.top=newitem
  def pop(self):
    if self.top is None:
      print("Stack is empty")
      return
    self.top=self.top.next
  def peek(self):
    if self.top is None:
      print("Peek is Not Possible")
      return
    print(f"Peek value is {self.top.data}")
  def isEmpty(self):
    if self.top is None:
      print(True)
    else:
      print(False)    
  def display(self):
    if self.top is None:
      print("Not Possible")
      return
    temp=self.top
    while temp!=None:
      print(f"{temp.data}=>",end=" ")
      temp=temp.next
    print("None")
st=Stack()
st.push(30)
st.push(40)
st.push(10)
st.pop()
st.display()
st.peek()

