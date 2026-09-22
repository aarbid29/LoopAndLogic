# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        dummy1 = ListNode(0)
        tail = dummy1
        curr = head
        curr2 = head

        dummy2 = ListNode(-1)
        tail2 = dummy2

        while curr:
            if curr.val < x:
                tail.next = curr
                tail = tail.next
            else:
                tail2.next = curr
                tail2 = tail2.next
            curr = curr.next
        tail2.next = None
        tail.next = dummy2.next
        return dummy1.next
        

    
    

        