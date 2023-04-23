class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class ll:
    def __init__(self):
        self.head = None
    def display(self):
        if self.head is None:
            print("list is empty")
        else:
            temp = self.head
            while temp:
              print(temp.data)
              temp = temp.next
l = ll()
n = Node(19)
l.head = n
n1 = Node(38)
l.head.next = n1
l.display()