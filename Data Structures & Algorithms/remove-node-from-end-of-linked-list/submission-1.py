# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        hp = head
        while(hp):
            length += 1
            hp = hp.next
        
        index = length - n
        if(index == 0):
            return head.next
        
        count = 0
        hp = head
        while(hp):
            if(count + 1 == index):
                hp.next = hp.next.next
            hp = hp.next
            count += 1

        return head

                














        
