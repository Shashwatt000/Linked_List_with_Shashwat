class binarytree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    def printtree(root):
      if root == None:
        return
      print(root.data , end = ":" )
      if root.left != None:
        print("L",root.left.data,end=',')
      if root.right != None:
        print("R",root.right.data)
      print()
      printtree(root.left)
      printtree(root.right)
bt1 = binarytree(1)
bt2 = binarytree(2)
bt3 = binarytree(3)
bt4 = binarytree(4)
bt5 = binarytree(5)
bt1.left = bt2
bt1.right = bt3
bt2.left = bt4
bt3.left = bt5
printtree(bt1)