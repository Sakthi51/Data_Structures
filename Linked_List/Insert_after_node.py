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



LL1 = LinkedList()
LL1.add_begin(10)
LL1.add_begin(20)
LL1.add_end(50)
LL1.add_end(30)
LL1.after_node(100, 10)

LL1.print_LL()
