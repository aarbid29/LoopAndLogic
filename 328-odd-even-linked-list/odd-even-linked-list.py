# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        odd = head
        even_beg = head.next
        even = head.next
        while odd.next and odd.next.next:
            next_odd = odd.next.next
            odd.next = odd.next.next
            even.next = next_odd.next
            
            odd = odd.next
            even = even.next
        
        odd.next = even_beg
        return head

        


