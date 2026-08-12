class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return None

        slow = head
        fast = head
        count = 0

        while fast and fast.next:
            count += 1
            slow = slow.next
            fast = fast.next.next

        nextt = slow.next

        curr = head
        prev = 0

        while prev < count - 1:
            curr = curr.next
            prev += 1

        curr.next = nextt

        return head