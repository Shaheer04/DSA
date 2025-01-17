class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

# Function to Print a LinkedList

def print_linked_list(head):
    while head is not None:
        print(head.value)
        head = head.next

# Function to Revesrve a Linkedlist Using Stack
def reverse_linked_list(head: Node) -> Node:
    stack = []
    currentNode = head

    # While loop to append linkedlist value in a stack
    while currentNode is not None:
        stack.append(currentNode.value)

        currentNode = currentNode.next

    reversedlist = Node(0)
    currentNode = reversedlist

    # for loop to assign values from stack to a reversed list in a reverse manner
    for i in range(len(stack)):

        currentNode.value = stack.pop()

        if len(stack) > 0:
            currentNode.next = Node()

        currentNode = currentNode.next

    return reversedlist

head = Node(1)
currentNode = head
for i in range (2, 6):
    currentNode.next = Node(i)
    currentNode = currentNode.next

print("=== Normal LinkedList ===")
print_linked_list (head)
print("=== Reverse LinkedList ===")
head =  reverse_linked_list(head)
print_linked_list(head)

