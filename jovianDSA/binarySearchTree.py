class BinarySearchTree:
  def __init__(self, val=None):
    self.value = val
    
    if self.value:
      self.left = BinarySearchTree()
      self.right = BinarySearchTree()
    else:
      self.left = None
      self.right = None
  
  def isempty(self):
    return self.value is None
  
  def isleaf(self):
    return self.left.isempty() and self.right.isempty()
  
  def maxvalue(self):
    if self.right.right == None:
      return self.value
    else:
      return self.right.maxvalue()
    
  def delete(self, v):
        if self.isempty():
            return
        if v < self.value:
            self.left.delete(v)
            return
        if v > self.value:
            self.right.delete(v)
            return
        if v == self.value:
            if self.isleaf():
                self.value = None
                self.left = None
                self.right = None
                return
            elif self.left.isempty():
                self.value = self.right.value
                self.left = self.right.left
                self.right = self.right.right
                return
            else:
                self.value = self.left.maxval()
                self.left.delete(self.left.maxval())
                return
  
  def insert(self,data):
        if self.isempty():
            self.value = data
            
            self.left = BinarySearchTree()
            self.right = BinarySearchTree()
            print("{} is inserted successfully".format(self.value))
            
        elif data < self.value:
            self.left.insert(data)
            return
          
        elif data > self.value:
            self.right.insert(data)
            
        elif data == self.value:
            return
  
  def find(self, x):
    if self.isempty():
      print("Tree is empty")
      return False
    if self.value == x:
      print("{} is found".format(x))
      return True
    if x < self.value:
      return self.left.find(x)
    else:
       return self.right.find(x)
  
  def inorder(self):
    if self.isempty():
      return []
    else:
      return self.left.inorder() + [self.value] + self.right.inorder()

  def preorder(self):
    if self.isempty():
      return []
    else:
      return [self.value] + self.left.preorder() + self.right.preorder()

  def postorder(self):
    if self.isempty():
      return []
    else:
      return self.left.postorder() + self.right.postorder() + [self.value]
    
  def height(self):
    if self.isempty():
      return 0
    else:
      return 1 + max(self.left.height(), self.right.height())
  
  def size(self):
    if self.isempty():
      return 0
    else:
      return 1 + self.left.size() + self.right.size()
  
  def is_balanced(self):
    if self.isempty():
      return True
    else:
      return (abs(self.left.height() - self.right.height()) <= 1) and self.left.is_balanced() and self.right.is_balanced()
    
  def make_balanced_bst(self, data, lo=0, hi=None, parent=None):
    if hi is None:
      hi = len(data) - 1
    if lo > hi:
      return None
    mid = (lo + hi) // 2
    root = BinarySearchTree(data[mid])
    root.left = self.make_balanced_bst(data, lo, mid - 1, root)
    root.right = self.make_balanced_bst(data, mid + 1, hi, root)
    return root
  
  def balance_bst(self):
    data = self.inorder()
    return self.make_balanced_bst(data)

def binary_search(arr, low, high, x):
    if len(arr) == 0:
        return -1

    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1
    
result = binary_search([12,13,14,15,16], 0, 4, 16)
print(result)

t = BinarySearchTree(15)
t.insert(10)
t.insert(18)
t.insert(4)
t.insert(11)
t.insert(16)
t.insert(20)
t.insert(13)
t.find(18)
print(t.inorder())
t.delete(13)
print("After deleting 13: ")
print(t.inorder())
print(t.preorder())
print(t.postorder())
print(t.height())
print(t.size())