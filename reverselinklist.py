class Node:
  def __init__(self,data):
    self.data = data
    self.next = None
class ll:
  def __init__(self):
    self.head = None
  def reverse_linklist(self):
    lali = self.head
    temp = self.head
    tempo = self.head 
    prev = None
    while temp.next: 
      #print("yaha aa gya")
      prev = tempo
      tempo = tempo.next
      temp = temp.next
    newnode = temp
    prev.next = None
    newnode.next = lali
    while newnode :
      print(newnode.data)
      newnode = newnode.next
  def display(self):
    temp = self.head
    while temp:
      print(temp.data,"-->",end=" ")
      temp = temp.next
l = ll()
n = Node(1)
l.head = n
n2 = Node(2)
n.next = n2
n3 = Node(3)
n2.next = n3
n4 = Node(4)
n3.next = n4
n5 = Node(5)
n4.next  = n5
#l.display()

l.reverse_linklist()
