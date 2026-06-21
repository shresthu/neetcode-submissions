# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #use 2 pointers
        prev,curr = None, head

        #while curr goes to the end and becomes None
        while curr:
            #store the next variable
            nxt = curr.next
            #join the head to the prev
            curr.next = prev
            #break the connection and move the curr forward
            prev = curr
            curr = nxt

        return prev
