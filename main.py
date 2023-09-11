class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# put a new element at the head of a linked list, with node containing new_data
# returns a pointer to the new node, which is the new head of the linked list
def insertAtFront(head_ptr, new_data):
    new_node = Node(new_data)
    new_node.next = head_ptr
    return new_node
# ------------------------------------------------------------------


def insertAtEnd(head_ptr, new_data):
    new_node = Node(new_data)

    if head_ptr is None:
        return new_node

    temp_ptr = head_ptr
    while temp_ptr.next is not None:
        temp_ptr = temp_ptr.next

    temp_ptr.next = new_node
    return head_ptr

# ------------------------------------------------------------------


def remove(head_ptr, element):
    # find and point at the element to remove. Also point at the previous element
    # This assumes that the element is in the linked list

    # removed = False     # initialize
    ptr = head_ptr

    # if the element is in the head, then just make the head_ptr into head_ptr.next
    if ptr.data == element:
        print("the head contains the node to remove")
        ptr = ptr.next
        print("ptr.data is: ", ptr.data)
        head_ptr = ptr
        return head_ptr

    # the element is not the head element. Find the right element
    prevPtr = head_ptr
    nextPtr = head_ptr.next

    # find the right node where the element is - currently assumes that the element is in the list
    while nextPtr.data != element:
        prevPtr = nextPtr
        nextPtr = nextPtr.next

    print("found the element. The data of the node is: ", nextPtr.data)

    # remove the element
    prevPtr.next = nextPtr.next

    return head_ptr
# ------------------------------------------------------------------


# assumes that the index is given as a correct index within the linked list
def removeAt(headPtr, index):
    prevPtr = headPtr
    nextPtr = prevPtr.next

    # remove the first element, which is at head
    if index == 0:
        headPtr = headPtr.next
        return headPtr

    # the element is not the first element. Point nextPtr at the element
    currentIndex = 1
    while index > currentIndex:
        prevPtr = nextPtr
        nextPtr = nextPtr.next
        currentIndex += 1

    # nextPtr is now pointing at the node to be removed
    prevPtr.next = nextPtr.next

    return headPtr

# ------------------------------------------------------------------

def printLinkedList(head_ptr):
    temp_ptr = head_ptr

    while temp_ptr is not None:
        print(temp_ptr.data, end=" ")
        temp_ptr = temp_ptr.next
    print("")

#----------------------------------------------------------------------------
if __name__ == '__main__':
    # Driver program
    head = None         # create a new list with no nodes

    head = insertAtFront(head, 7)
    head = insertAtFront(head, 34)
    head = insertAtFront(head, 19)
    print("Printing linked list after first 3 elements added to front of list")
    printLinkedList(head)

    print("Printing linked list after one more element added to end of list")
    head = insertAtEnd(head, 25)
    printLinkedList(head)

    print("Printing linked list after one more element added to end of list")
    head = insertAtEnd(head, 126)
    printLinkedList(head)

    head2 = None
    print("Printing linked list that has no elements")
    printLinkedList(head2)

    head2 = insertAtFront(head2, 7)
    print("Printing linked list with one element, added to the front")
    printLinkedList(head2)

    head2 = None
    head2 = insertAtEnd(head2, 115)
    print("Printing linked list with one element, added to the end")
    printLinkedList(head2)

    print("The linked list before remove function is: ")
    printLinkedList(head)
    print("going into remove function now, removing element 126")
    head = remove(head, 126)
    printLinkedList(head)

    print("removing the first node in the list. ")
    print("The linked list before removing anything is:")
    printLinkedList(head)
    head = removeAt(head, 0)
    print("The linked list after removing the header node is:")
    printLinkedList(head)

    head = removeAt(head, 1)
    print("The linked list after removing node 1, which is 7, is:")
    printLinkedList(head)

    head = removeAt(head, 1)
    print("The linked list after removing node 1, which is 25, is:")
    printLinkedList(head)
