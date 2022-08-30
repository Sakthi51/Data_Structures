queue = []
def enqueue():
     element = int(input("Enter element : "))
     queue.append(element)
     print(f"Element {element} is added")
def dequeue():
    if not queue:
        print("Queue is empty")
    else:
        element = queue.pop(0)
def display():
    print(queue)

while True:
    print("Select options 1:Enqueue 2:Dequeue 3:Display 4:Exit")
    choice = int(input())
    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        display()
    elif choice == 4:
        break
    else:
        print("Enter a valid option")
