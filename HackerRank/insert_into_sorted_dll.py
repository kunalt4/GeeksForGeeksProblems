

# Complete the sortedInsert function below.

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
def sortedInsert(head, data):
    
    node = DoublyLinkedListNode(data)
    if not head:
        head = node
        return head

    temp = preTemp = head

    while(temp and data >= temp.data):
        preTemp = temp
        temp = temp.next
    
    if not temp:
        preTemp.next = node
        node.prev = preTemp
    
    elif not temp.prev:
        temp.prev = node
        node.next = temp
        head = node
    
    else:
        temp.prev = node
        node.next = temp
        preTemp.next = node
        node.prev = preTemp

    return head


