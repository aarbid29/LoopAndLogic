from collections import defaultdict

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node(0)
        tail = dummy
        mp = defaultdict()
        curr = head

        while curr:
            if curr not in mp:
                new_node = Node(curr.val)
                mp[curr] = new_node
            else:
                new_node = mp[curr]

            original_random = curr.random
            if original_random:
                if original_random not in mp:
                    new_nodee = Node(original_random.val)
                    new_node.random = new_nodee
                    mp[original_random] = new_nodee
                else:
                    new_node.random = mp[original_random]
            curr = curr.next

            tail.next = new_node
            tail = tail.next

        return dummy.next

        