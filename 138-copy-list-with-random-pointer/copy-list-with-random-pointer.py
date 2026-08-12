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

        dummy = Node(0)
        mp = defaultdict()
        tail = dummy
        curr = head 

        while curr:
            if curr not in mp:
                new_node = Node(curr.val)
                mp[curr] = new_node
            else:
                new_node = mp[curr]

            random = curr.random #random of original
            if random:
                if random in mp:
                    new_node.random = mp[random]
                else:
                    create = Node(random.val)
                    new_node.random = create
                    mp[random] = create
            
            curr = curr.next
            tail.next = new_node
            tail = tail.next
        return dummy.next

        