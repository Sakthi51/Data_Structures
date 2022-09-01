class Node():
    def __init__(self, data):
        self.data = data
        self.nref = None
        self.pref = None

class DoublyLinkedList():
    def __init__(self):
        self.head = None
    # Forward Traversal
    def print_LL(self):
        if self.head == None:
            print("Linked List is empty!!!")
        else:
            n = self.head
            while n != None:
                print(n.data, '--->', end=' ')
                n = n.nref

    # Backward Traversal
    def print_LL_reverse(self):
        print()
        if self.head == None:
            print("Linked List is empty!!!")
        else:
            n = self.head
            while n.nref != None:       # Traversal without printing data
                n = n.nref
            while n != None:
                print(n.data, '--->', end= ' ')
                n = n.pref

    def insert_empty(self, data):
        if self.head == None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("Linked list is empty")

    

DLL1 = DoublyLinkedList()
DLL1.insert_empty(10)
DLL1.print_LL()
DLL1.print_LL_reverse()


