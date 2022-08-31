# empty node to use
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
            while n.ref != None:  # traverse until head reference becomes null
                n = n.ref
            n.ref = new_node      # new node is the last node added, so reference number of last node is save to head node(previous node)
            

LL1 = LinkedList()
LL1.add_begin(10)
LL1.add_end(50)
LL1.add_end(100)
LL1.add_begin(20)
LL1.print_LL()
