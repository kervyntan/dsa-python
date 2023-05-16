# Array vs LinkedList
# Array -> collection of data items of the same type 
# LinkedList -> Collection of the same data type stored sequentially and connected through pointers

# Suitability
# Arrays -> when we need to do a lot of accessing, and fewer insertion/deletion operations (since the array size is static)
# LinkedList -> Are suitable in applications where the size of the list is not fixed, and a lot of insertion/deletion operations will be required

# LinkedList properties
# - Elements are stored in memory in different locations that are connected through pointers
# Pointers are objects that store the **memory addresses of a variable(s), and each data element points to the next data element, last one points to None 
# - Length of list can increase or decrease during execution of the program

# Nodes & Pointers
# Node - a container of data, together with one or more links to others nodes where a link is a Pointer

class Node:
    def __init__(self, data=None):
        # Can add other data items to the node class if required
        # eg. if the node is going to contain Customer data, then create a Customer clas and place the data there
        self.data = data
        # Initialiaed next pointer to None
        self.next = None


# Traversing the list 

# Singly Linked List 
def naiveTraverseSingly():
    n1 = Node("eggs")
    n2 = Node("ham")
    n3 = Node("spam")

    # Linking nodes (last node for singly linked points to None) 
    n1.next = n2
    n2.next = n3 

    current = n1
    while current:
        print(current.data)
        current = current.next

# naiveTraverseSingly()

def improvedTraverseSingly(self):
    current = self.head
    while current:
        val = current.data
        current = current.next
        # "yield" used to return from a function while saving the states of its local variables 
        # Enables the function to resume from where it left off
        # Whenever the function is called again, execution begins from the last yield statement
        yield val

    # Inserting data item


class NaiveSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    

    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
                print("appended")
            current.next = node

words = NaiveSinglyLinkedList()
words.append("eggs")
words.append("ham")
words.append("spam")

class SinglyLinkedList():
    def __init__(self):
        self.tail = None
        self.head = None
        self.size = 0

    def append(self, data):
        node = Node(data)
        if self.tail:
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node 

words = SinglyLinkedList()
words.append("eggs")
words.append("ham")
words.append("spam")
current = words.head

while current:
    print(current.data)
    current = current.next
    # Deleting data item

        
