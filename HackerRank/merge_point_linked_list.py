

# Complete the findMergeNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def findMergeNode(head1, head2):
    temp1 = head1
    temp2 = head2
    count1 = count2 = 0

    while(temp1):
        count1+=1
        temp1 = temp1.next

    while(temp2):
        count2+=1
        temp2 = temp2.next
    
    temp1 = head1
    temp2 = head2

    diff = abs(count1-count2)

    if count1 > count2:
        for _ in range(diff):
            temp1 = temp1.next
    else:
        for _ in range(diff):
            temp2 = temp2.next

    while(temp1!=temp2):
        temp1 = temp1.next
        temp2 = temp2.next
        
    return temp1.data
