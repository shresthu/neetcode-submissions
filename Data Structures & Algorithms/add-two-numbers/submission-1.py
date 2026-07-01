# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()

        temp = dummy

        carry = 0
        while l1 or l2 or carry:
            #extract the values of the nodes
            d1 = l1.val if l1 else 0
            d2 = l2.val if l2 else 0

            sum_val = d1 + d2 + carry
            carry = sum_val // 10 #this holds the carry over value which is either 1 or 0
            val = sum_val % 10 #the value which is to be stored in the node

            temp.next = ListNode(val) #add a new node which hold the new value and point temp to it

            temp = temp.next 
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next







