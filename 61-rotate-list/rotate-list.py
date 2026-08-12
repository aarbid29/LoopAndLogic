class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        num = 0
        n = head
        while n:
            num += 1
            n = n.next

        k %= num
        if k == 0:
            return head

        step = 0
        prev = head
        curr = head

        while curr and step < num - k:
            prev = curr
            step += 1
            curr = curr.next

        headd = curr

        while curr.next:
            curr = curr.next

        curr.next = head
        prev.next = None

        return headd