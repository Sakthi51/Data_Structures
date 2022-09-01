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

    def insert_begin(self, data):
        if self.head == None:
            new_node = Node(data)
            self.head = new_node
        else:
            new_node = Node(data)
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node

    def insert_end(self, data):
        new_node = Node(data)
        if self.head == None:
             self.head = new_node
        else:
            n = self.head
            while n.nref != None:
                n = n.nref
            n.nref = new_node
            new_node.pref = n


DLL1 = DoublyLinkedList()
DLL1.insert_begin(10)
DLL1.insert_begin(20)
DLL1.insert_end(30)
DLL1.print_LL()
DLL1.print_LL_reverse()


