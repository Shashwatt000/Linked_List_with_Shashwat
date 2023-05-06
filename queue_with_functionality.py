class Node:
  def __init__(self,data):
    self.data = data
    self.next = None
class Queue:
  def __init__(self):
    self.head = None
  
  
  def enqueue(self,data):
    temp = self.head
    tempo = self.head
    while tempo.next:
      tempo = tempo.next
    tempo.next = Node(data)
  
  def peek(self):
    temp = self.head
    print(temp.data)
  
  def dequeue(self):
    temp = self.head
    tempo = temp.next
    self.head = tempo
    
  def size(self):
    temp = self.head
    count = 0
    while temp is None:
      print("size of queue is 0")
    while temp:
      count = count+1
      temp = temp.next
    print(count)
  
  def display(self):
    temp = self.head
    while temp:
      print(temp.data)
      temp = temp.next
q = Queue()
n = Node(1)
n1 = Node(2)
n.next = n1
n2 = Node(3)
n1.next = n2
n3 = Node(4)
n2.next = n3
n4 = Node(5)
n3.next = n4
q.head = n
q.enqueue(6)
q.dequeue()
q.display()
q.peek()
q.size()