class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

#we initiated a Node class

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity #save the capacity
        self.cache = {} # here we will map the key to a Node

        #we need to have 2 pointers nodes
        # Left and right within which we have the LRU cache nodes
        self.left, self.right = Node(0,0),Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    #helper function to have the removal of node.
    def remove(self,node):
        previous = node.prev #store the previous of the current node
        nxt = node.next #store the next of the node
        previous.next = nxt #point the previous node to the next pointer of current node
        nxt.prev = previous #point the prev of next pointer to the previous of the current node

    #helper function to have addition of node to the right side
    def insert(self,node):
        previous = self.right.prev #store the previous as second last node (before the self.right)
        nxt = self.right #store the next as last node(self.right)
        previous.next = node # previous should point the the new node
        nxt.prev = node #next node(right side) previous should point to the node
        node.next = nxt #node next should point to self.right 
        node.prev = previous #node previous should point to the third last element since new node is second last now

    def get(self, key: int) -> int:
        #if we find the key in the helper function
        if key in self.cache:
            self.remove(self.cache[key]) #if key exists, we have to remove from the left pointer(LRU) since it is used 
            self.insert(self.cache[key]) # and add it to the right pointer since most recently used
            return self.cache[key].val 
        return -1

    def put(self, key: int, value: int) -> None:
        #check if the key exists in the cache, if so we have to remove from left since most recently use
        if key in self.cache:
            self.remove(self.cache[key]) #since we have, we remove from left side (LRU)

        self.cache[key] = Node(key,value) #add a new node with key value
        self.insert(self.cache[key]) #regardless add to the right side of the cache

        #check if we reach or exceed the capacity
        if len(self.cache) > self.capacity:
            least_recently_used = self.left.next  #LRU is the next of left pointer
            self.remove(least_recently_used) #remove the node
            del self.cache[least_recently_used.key] #remove it from cache
        



























