class Node:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next  = next

    def __str__(self):
        return str(self.cargo)

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.next = node2
node2.next = node3

def print_list(node):
    while node is not None:
        print(node, end=" ")
        node = node.next
    print()

#print_list(node1)

'''
#Longer, more easy to understand version of print_backwards:
def print_backward(list):
    if list is None: return
    head = list
    tail = list.next
    print_backward(tail)
    print(head, end=" ")
'''

#Shorter, more difficult to understand version of print_backwards:
def print_backward(list):
    if list is None: return
    print_backward(list.next)
    print(list, end=" ")

#print_backward(node1)

def remove_second(list):
    if list is None: return
    first = list
    second = list.next
    # Make the first node refer to the third
    first.next = second.next
    # Separate the second node from the rest of the list
    second.next = None
    return second

#removed = remove_second(node1)
#print_list(removed)
#print_list(node1)

def print_backward_nicely(list):
    print("[", end=" ")
    print_backward(list)
    print("]")

#print_backward_nicely(node1)

class LinkedList:

    def __init__(self):
        self.length = 0
        self.head = None
    '''
    def print_backward(self):
        print("[", end=" ")
        if self.head is not None:
            self.head.print_backward()
    '''
    def add_first(self, cargo):
        node = Node(cargo)
        node.next = self.head
        self.head = node
        self.length += 1

#EXERCISE 1:
def print_list_nicely(node):
    print("[", end="")
    while node is not None:
        if node.next == None:
            print(node, end="]")
            break
        print(node, end=", ")
        node = node.next

print_list_nicely(node1)