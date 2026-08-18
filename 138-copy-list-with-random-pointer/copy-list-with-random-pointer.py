class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        mp = {}
        curr = head
        s_curr = head
        while curr:
            new_node = Node(curr.val)
            mp[curr] = new_node
            curr = curr.next

        while s_curr:
            cop = mp[s_curr]

            if s_curr.next in mp:
                cop.next = mp[s_curr.next]
            else:
                cop.next = None

            if s_curr.random in mp:
                cop.random = mp[s_curr.random]
            else:
                cop.random = None

            s_curr = s_curr.next

        return mp[head]
