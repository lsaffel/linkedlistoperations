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


def insertAtEnd(head_ptr, new_data):
    new_node = Node(new_data)

    if head_ptr is None:
        return new_node

    temp_ptr = head_ptr
    while temp_ptr.next is not None:
        temp_ptr = temp_ptr.next

    temp_ptr.next = new_node
    return head_ptr


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
