

# Complete the reverse function below.

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
def reverse(head):
    curr = head
    temp = head.next
    while temp:
        curr.next = curr.prev
        curr.prev = temp
        curr = temp
        temp = temp.next
    curr.next = curr.prev
    curr.prev = None
    return curr

