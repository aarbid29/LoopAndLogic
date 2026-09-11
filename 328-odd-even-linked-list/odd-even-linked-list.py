# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        beg = head
        odd_head = head
        even_head = head.next
        ag = head.next



        while odd_head.next and odd_head.next.next :
            odd_next = odd_head.next.next
            odd_head.next = odd_next
            odd_head = odd_next

            even_next = even_head.next.next
            even_head.next = even_next
            even_head = even_next

        odd_head.next = ag
        return beg

        






            




        