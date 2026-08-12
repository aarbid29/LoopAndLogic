class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = head
        num = 0

        while n:
            n = n.next
            num += 1

        dummy = ListNode()
        dummy.next = head

        prev_group_end = dummy
        curr = head
        globall = 0

        while curr:
            if num - globall < k:
                break

            first = curr
            prev = prev_group_end
            track = 0

            while track < k:
                nextt = curr.next
                curr.next = prev
                prev = curr
                curr = nextt
                track += 1
                globall += 1

            prev_group_end.next = prev
            first.next = curr
            prev_group_end = first

        return dummy.next