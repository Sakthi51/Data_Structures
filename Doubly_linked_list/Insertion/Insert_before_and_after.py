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

    def insert_after(self, data, x):
        if self.head == None:
            print("Linked list is empty")
        else:
            n = self.head
            while n != None:
                if x == n.data:
                    break
                n = n.nref
            if n == None:
                print("Given node is not present in th list")
            elif n.nref == None:
                new_node = Node(data)
                n.nref = new_node
                new_node.pref = n
            else:
                new_node = Node(data)
                new_node.nref = n.nref
                new_node.pref = n
                if n.nref != None:          # condition if it is a last node
                    n.nref.pref = new_node
                n.nref = new_node

    def insert_before(self, data, x):
        new_node = Node(data)
        if self.head == None:
            print("Linked list is empty")
        else:
            n = self.head
            while n != None:
                if x == n.data:
                    break
                n = n.nref
            if n.nref == None:
                print("Given node is not present in linked list")
            else:
                new_node.nref = n
                new_node.pref = n.pref
                if n.pref != None:          # condition to add before first element
                    n.pref.nref = new_node
                else:
                    self.head = new_node
                n.pref = new_node

  


DLL1 = DoublyLinkedList()
DLL1.insert_begin(10)
DLL1.insert_begin(4)
DLL1.delete_by_value(10)
DLL1.print_LL()
DLL1.print_LL_reverse()


