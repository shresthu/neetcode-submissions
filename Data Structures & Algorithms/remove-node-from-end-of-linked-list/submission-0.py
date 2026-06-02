# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        hp =  head
        count = start = 0
        #got the length of the list
        while(hp):
            hp = hp.next
            count += 1
        
        #use the legth to find the index of the value to be removed from start
        index = count - n
        hp = head
        if index == 0:
            return head.next

        while(hp):
            if(hp.next and index - 1 == start):
                hp.next = hp.next.next
            hp = hp.next
            start += 1
        
        return head
                














        
