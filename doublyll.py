class Node:
  def __init__(self,data):
    self.data=data
    self.prev=None
    self.next=None

class LinkedList:
  def __init__(self):
    self.head=None
  def insert_at_begin(self,data):
    newnode=Node(data)
    if self.head is None:
      self.head=newnode
      return
    newnode.next=self.head
    self.head.prev=newnode
    self.head=newnode
  def insert_at_end(self,data):
    newnode=Node(data)
    if self.head is None:
      self.head=newnode
      return
    temp=self.head
    while temp.next!=None:
      temp=temp.next
    temp.next=newnode
    newnode.prev=temp
  def insert_at_pos(self,data,index):
    newnode=Node(data)
    if self.head is None:
      if index==0:
        newnode.next=self.head
        self.head.prev=newnode
        self.head=newnode
        return
      else:
        print("Index Out of Range")
        return
    temp=self.head
    for i in range(index-1):
      if temp is None:
        print("Index Out of range")
        return
      temp=temp.next
    if temp is None:
        print("Index Out of range")
        return
    if temp.next!=None:
      newnode.next=temp.next
      temp.next.prev=newnode
      newnode.prev=temp
      temp.next=newnode
    else:
      temp.next=newnode
  def delete_at_begin(self):
    if self.head is None:
      print("Not Posible")
    self.head=self.head.next
    self.head.prev=None
  def delete_at_end(self):
    if self.head is None:
      print("Not Posible")
      return
    temp=self.head
    while temp.next.next!=None:
      temp=temp.next
    temp.next=None
  def delete_at_pos(self,index):
    if self.head is None:
      print("Not Posible")
      return
    temp=self.head
    for i in range(index-1):
      if temp is None:
        print("Index Out of range")
        return
      temp=temp.next
    if temp is None:
        print("Index Out of range")
        return
    if temp.next.next is None:
      temp.next=None
    else:
      temp.next=temp.next.next
      temp.next.prev=temp
  def traverse(self):
    if self.head is None:
      print("No elements found")
      return
    temp=self.head
    while temp!=None:
      print(f"{temp.data}",end="<=>")
      temp=temp.next
    print("None")
dll=LinkedList()
dll.insert_at_begin(10)
dll.insert_at_begin(20)
dll.insert_at_begin(40)
dll.insert_at_begin(19)
dll.insert_at_end(29)
dll.insert_at_pos(2,2)
dll.delete_at_begin()
dll.insert_at_pos(40,5)
dll.delete_at_end()
dll.delete_at_pos(4)
dll.traverse()