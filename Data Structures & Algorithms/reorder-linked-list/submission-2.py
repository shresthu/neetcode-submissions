class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #firstly lets find the mid point of the array and then we will reverse the string 
        #which comes after that and then just merge the 2.

        slow,fast = head,head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #now that we have moved the pointers such that slow is at the mid of the list
        #second list will start from the next element of the middle point
        second_list_end = slow.next

        #now lets reverse the second list
        #but first lets break the conection between first and second list
        slow.next = None
        
        #simple reversal structure followed
        prev = None
        curr = second_list_end

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        second_list_start = prev

        #now we have 2 lists from the first one with first ascending and second decending
        #now we have to merge both the lists
        first,second = head,second_list_start

        #becuase second could be shorter traverse:
        while second:
            #lets store the next values of each list
            temp_first, temp_second = first.next, second.next
            first.next = second
            second.next = temp_first
            first = temp_first
            second = temp_second




























