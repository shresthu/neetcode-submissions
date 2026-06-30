"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_to_copy = {None:None}

        cur = head
        #first pass to create the hasmap
        while cur:
            copy = Node(cur.val)
            old_to_copy[cur] = copy
            cur = cur.next
        
        #now that we have created copy nodes and populated hashmap

        cur = head
        while cur:
            #curr pointing to copy so extract that copy
            copy = old_to_copy[cur]
            #copy would point to the curr element next
            copy.next = old_to_copy[cur.next]
            #copy.random will point to the value of node which points to random
            copy.random = old_to_copy[cur.random]
            cur = cur.next
        
        return old_to_copy[head]

















