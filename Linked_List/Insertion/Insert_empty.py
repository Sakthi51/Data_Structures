# added insert_empty class
class Node():
    def __init__(self, data):
        self.data = data
        self.ref = None

class LinkedList():
    def __init__(self):
        self.head = None

    def print_LL(self):
        if self.head == None:
            print("Linked List is empty!!!")
        else:
            n = self.head
            while n != None:
                print(n.data, '--->', end=' ')
                n = n.ref

    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_end(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            n = self.head
            while n.ref != None:
                n = n.ref
            n.ref = new_node

    def after_node(self, data, x):  # we don't know where to add the value so, we have to find the x first
        n = self.head               # data = which number we want to enter
        while n != None:            # x = where we want to enter the number
            if x == n.data:          # traversal to search for x. if found break, else move to the next node
                break
            n = n.ref
        if n == None:
            print("Node is not present in LL")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def before_node(self, data, x):
        if self.head == None:               # if LL is empty can't add before
            print("Linked list is empty")
            return                          # stop here, don't execute the code after this
        if self.head.data == x:             # if value of head node and x is same add at the beginning
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return                          # stop here, don't execute the code after this
        n = self.head
        while n.ref != None:
            if n.ref.data == x:             # find the x and find the previous node to use add after the node
                break
            n = n.ref
        if n.ref == None:                   # before finding x if it reaches null, print not found
            print("Node is not found")
        else:
            new_node = Node(data)           # add after code snippet
            new_node.ref = n.ref
            n.ref = new_node

    def insert_empty(self, data):
        if self.head == None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("Linked list is not empty")



LL1 = LinkedList()
LL1.insert_empty(10)

LL1.print_LL()
