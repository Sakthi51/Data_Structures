# Create a empty head node
# self.head = pointer
# self.head.data = value stored in the pointer
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
                print(n.data)
                n = n.ref

LL1 = LinkedList()
LL1.print_LL()
