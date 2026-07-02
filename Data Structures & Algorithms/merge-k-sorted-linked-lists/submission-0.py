# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        
        while len(lists) > 1: #divide and conquer apporach so we are just going to bring it till the last value
            mergedLists = [] #this will hold the temp merged lists
            for i in range(0,len(lists),2): #pick first 2 merge, pick next 2 merge 
                l1 = lists[i]
                l2 = lists[i+1] if (i+1) < len(lists) else None 
                
                mergedLists.append(self.mergeList(l1,l2))
            lists = mergedLists #now the lists becomes half of initial value and merge again
        return lists[0]


    #merge.   1 -> 2 -> 4 
    #and      1 -> 3 -> 5 -> 6

    #helper function to merge 2 lists
    def mergeList(self,l1,l2):
        dummy = ListNode()

        tail = dummy

        while l1 and l2:
            if l1.val > l2.val:
                tail.next = l2
                l2 = l2.next
            else:
                tail.next = l1
                l1 = l1.next
            
            tail = tail.next
        
        if l1:
            tail.next = l1
        
        if l2:
            tail.next = l2
        
        return dummy.next






















        

