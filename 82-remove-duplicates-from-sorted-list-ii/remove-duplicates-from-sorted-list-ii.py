class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode(0)
        dummy.next  = head

        prev = dummy
        curr = head
        while curr and curr.next :
            if curr.val == curr.next.val:
                val = curr.val
                while curr.val ==val:
                    curr = curr.next
                    if curr == None:
                        break
                prev.next = curr
                # curr =curr.next
                continue
            prev = curr
            curr = curr.next

        return dummy.next



        