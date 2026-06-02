# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
            slow,fast = head, head.next

            #finding the start of second half of list
            while(fast and fast.next):
                slow = slow.next
                fast = fast.next.next

            #here setting the start of second array and setting
            # the pointing the last of the first half as null
            second = slow.next
            slow.next = None

            #reverse the second array, second is the start of the array
            #go to the end of the list and store the next value in tmp
            tmp_node = None
            while(second):
                tmp = second.next
                second.next = tmp_node
                tmp_node = second
                second = tmp

            #reversed and now we have two pointers, one pointing at head and
            #another at end which is going to be tmp_node
            #merge lists starting from head(l1) and tmp_node(l2)

            first, second = head, tmp_node #setting start of first and second list
            while second: #go through the second list
                #store first ka next in tm1 and second ka next in tmp2
                tmp1, tmp2 = first.next, second.next 
                #put first ka next as second(start of second list)
                first.next = second
                #put second.next = tmp1 which is first ka next
                second.next = tmp1
                #put first
                first = tmp1
                second =  tmp2
                





































            