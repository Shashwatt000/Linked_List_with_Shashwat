class Node:
  def __init__(self,data):
    self.data = data
    self.next = None
class ll:
  def __init__(self):
    self.head = None
  def remove_duplicate(self):
    temp = self.head
    tempo = temp.next
    pre = None
    while tempo:
     
      if temp.data == tempo.data :
        tempo = tempo.next
        pre = temp
        temp = temp.next
       
      else:
        temp.next = tempo
     

      tempo = tempo.next
      pre = temp
      temp = temp.next
      if pre.data != temp.data:
        print(pre.data,"-->",end="")
    print(temp.data)
   
  def display(self):
    temp = self.head
    while temp:
      print(temp.data,"-->",end=" ")
      temp = temp.next
l = ll()
n = Node(1)
l.head = n
n1 = Node(1)
l.head.next = n1
n2  = Node(2)
n1.next = n2
n3 = Node(2)
n2.next = n3
n4 = Node(3)
n3.next = n4
n5 = Node(3)
n4.next = n5
n6 = Node(4)
n5.next = n6
n7 = Node(4)
n6.next = n7
n8 = Node(4)
n7.next = n8
n9 = Node(5)
n8.next = n9
l.display()
print()
l.remove_duplicate()