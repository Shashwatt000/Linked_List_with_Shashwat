class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def length(head):
      count = 0 
      while head is not None:
        count = count+1
        head = head.next
        return count
class ll:
    def __init__(self):
        self.head = None
    def insert_begin(self,data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
    def insert_end(self,data):
        neend = Node(data)
        temp = self.head
        while temp:
          if temp.next == None:
            temp.next = neend
            break
          temp = temp.next
    def insert_position(self,pos,data):
      np = Node(data)
      count = 0 
      pre = None
      curr = self.head
      while count < pos:
        pre = curr
        curr = curr.next
        count = count + 1
      pre.next = np
      np.next = curr
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
l.insert_begin(17)
l.insert_begin(24)
l.insert_end(69)
l.insert_end(98)
l.insert_position(2,11)
l.display()