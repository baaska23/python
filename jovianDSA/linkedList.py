class LinkedList:
  def __init__(self, nodes=None):
    self.head = None
    if nodes is not None:
        node = Node(data=nodes.pop(0))
        self.head = node
        for elem in nodes:
            node.next = Node(data=elem)
            node = node.next
  
  def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("Null or None")
        return " -> ".join(nodes)
  
  def __iter__(self):
    node = self.head
    while node is not None:
        yield node
        node = node.next

  def add_first(self, node):
     node.next = self.head
     self.head = node
  
  def add_last(self, node):
    if self.head is None:
        self.head = node
        return
    else:
        for current_node in self:
            pass
        current_node.next = node
  
  def add_after(self, target_node_data, new_node):
    if self.head is None:
        raise Exception("List is empty")
    for node in self:
        if node.data == target_node_data:
            new_node.next = node.next
            node.next = new_node
            return
  
  def add_before(self, target_node_data, new_node):
    if self.head is None:
        raise Exception("List is empty")
    if self.head.data == target_node_data:
        return self.add_first(new_node)
    else:
        node = self.head
        while node.next.data != target_node_data:
            node = node.next
        new_node.next = node.next
        node.next = new_node
  
  def remove_node(self, target_node_data):
    if self.head is None:
        raise Exception("List is empty")
    if self.head.data == target_node_data:
        self.head = self.head.next
        return
    else:
        node = self.head
        while node.next.data != target_node_data:
            node = node.next
        node.next = node.next.next
    
  def reverse(self, head):
    prev = None
    current = head
    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev

class DoubleLinkedList():
  def __init__(self, nodes=None):
    self.head = None
    if nodes is not None:
        node = Node(data=nodes.pop(0))
        self.head = node
        for elem in nodes:
            node.next = Node(data=elem)
            node = node.next

class CircularLinkedList():
  def __init__(self, nodes=None):
    self.head = None
    if nodes is not None:
        node = Node(data=nodes.pop(0))
        self.head = node
        for elem in nodes:
            node.next = Node(data=elem)
            node = node.next
            node.next = self.head
  
  def traverse(self, starting_point=None):
    if starting_point is None:
      starting_point = self.head
    node = starting_point
    while node.next != starting_point:
      print(node.data)
      node = node.next
    print(node.data)

  def __repr__(self):
    node = self.head
    nodes = []
    while node.next != self.head:
      nodes.append(node.data)
      node = node.next
    nodes.append(node.data)
    return " -> ".join(nodes)
  
  def print_list(self, starting_point=None):
    nodes = []
    for node in self.traverse(starting_point):
        nodes.append(str(node))
    print(" -> ".join(nodes))

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
  
  def __repr__(self):
    return self.data

llist = LinkedList()
first_node = Node("Monday")
llist.head = first_node

second_node = Node("Tuesday")
third_node = Node("Wednesday")

first_node.next = second_node
second_node.next = third_node
print(llist)

#Traverse = Iterate
another_list = LinkedList(["a", "b", "c", "d", "e"])
for node in another_list:
    print(node)
  
another_list.add_first(Node("first"))
another_list.add_last(Node("last"))
another_list.add_after("b", Node("after b"))
another_list.add_before("c", Node("before c"))
another_list.remove_node("e")
print(another_list)
