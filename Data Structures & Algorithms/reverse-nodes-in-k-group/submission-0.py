# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0,head) #dummy node which points to the head
        groupPrev = dummy #previous group which points to the dummy variable

        #we are starting with 1 node behind the head 
        while True:
            kth = self.getKth(groupPrev,k)
            if not kth: #essentially kth return Null, means not enough numbers so break
                break
            groupNext = kth.next

            #reverse the list
            prev = kth.next
            curr = groupPrev.next

            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            #now that we have reveresed the list we have to move the pointers around
            #to attach the new head 


            tmp = groupPrev.next #store the next of previous group 
            groupPrev.next = kth #now the head pointer will point to the new start i.e. kth
            groupPrev = tmp #the group now moves to the next element of kth.

        return dummy.next


    
    #this return the kth number from current start
    def getKth(self,curr,k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        
        return curr
