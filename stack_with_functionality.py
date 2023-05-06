class Node:
  def __init__(self,data):    
    self.data = data
    self.next = None
 
class Stack:
  def __init__(self):
    self.head = None
  def isEmpty(self):
    temp = self.head
    if temp is None:
      print("true")
    else:
      print("false")
  def top(self):
    temp = self.head
    while temp.next:
      temp = temp.next
    print(temp.data)
  def pop(self):
    temp = self.head
    curr = None
    while temp.next:
      curr = temp
      temp = temp.next
    temp = self.head
    curr.next = None
  def push(self,data):
    temp = self.head
    while temp.next:
      temp = temp.next
    temp.next = Node(data)
   
  def size(self):
    temp = self.head
    count = 0
    if temp is None:
      print("size is 0")
    while temp:
      temp = temp.next
      count = count + 1
    print("size of stack is",count)
   
  def display(self):
    temp = self.head
    while temp:
      print(temp.data)
      temp = temp.next
s = Stack()
n = Node(5)
s.head = n
n1 = Node(10)
n.next = n1
n2 = Node(15)
n1.next = n2
s.push(20)
s.push(25)
s.pop()
s.display()
s.size()
s.top()
s.isEmpty()
