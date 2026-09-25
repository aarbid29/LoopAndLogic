# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        n = 0 
        x = head
        while x:
            x = x.next
            n+=1
        dummy = ListNode()
        dummy.next = head
        tail = dummy 
        prevgroupend = dummy
        prev =prevgroupend
        curr = head
        globall = 0
        track = 0

        while curr:
            if n - globall < k:
                break
            first = curr
            track = 0 
            
            while track < k:
                track+=1
                nextt = curr.next
                curr.next = prev
                prev = curr
                curr = nextt
                globall+=1
            
            prevgroupend.next = prev
            prevgroupend = first 
            first.next = curr
            prev = prevgroupend

        return dummy.next

            
            


        
        