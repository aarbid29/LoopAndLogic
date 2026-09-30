# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        if not head:
            return None
        n = 0
        x = head
        while x:
            n +=1
            x = x.next
        
        dummy = ListNode(0,head)
        
        tail = dummy 
        prevgroupend = dummy
        globall = 0 
        track = 0
        first = None
        curr = head

        while curr:

            if n-globall< 2:
                break
            
            first = curr
            prev = prevgroupend
            track =0

            while track<2:
                nextt = curr.next
                curr.next = prev
                prev = curr
                curr = nextt
                globall+=1
                track+=1
            
            first.next = curr
            prevgroupend.next = prev
            prevgroupend = first
        
        return dummy.next



            



        