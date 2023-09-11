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


def printLinkedList(head_ptr):
    print("Printing linked list -------------------")
    temp_ptr = head_ptr

    while temp_ptr is not None:
        print(temp_ptr.data, end=" ")
        temp_ptr = temp_ptr.next


if __name__ == '__main__':
    # Driver program
    head = None         # create a new list with no nodes

    head = insertAtFront(head, 7)
    head = insertAtFront(head, 34)
    head = insertAtFront(head, 19)
    printLinkedList(head)