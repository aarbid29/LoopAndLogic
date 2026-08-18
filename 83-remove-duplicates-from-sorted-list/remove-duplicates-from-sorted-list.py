class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr:
            
            nextt = curr.next

            while nextt and nextt.val == curr.val:
                nextt = nextt.next

            curr.next = nextt
            curr = curr.next

        return head