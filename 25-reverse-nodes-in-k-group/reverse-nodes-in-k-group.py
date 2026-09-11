# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        n = 0 
        x = head
        while x :
            n+=1
            x =x.next

        curr = head
        prev = None
        dummy = ListNode()
        dummy.next = head
        prev_group_end = dummy
        globall = 0

        while curr:
            if n-globall <k:
                break

            first = curr
            prev = prev_group_end
            track = 0

            while track < k:
                #reverse it 
                nextt = curr.next
                curr.next = prev
                prev = curr
                curr = nextt
                track+=1
                globall +=1
            
            first.next = curr
            prev_group_end.next = prev
            prev_group_end = first
        
        return dummy.next
        

            

            








        

        

        
        



        