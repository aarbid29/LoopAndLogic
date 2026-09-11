# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr1 = head
        prev = None
        lenn = 0 
        #FIRST REVERSING 
        while curr1:
            lenn+=1
            nextt =curr1.next
            curr1.next = prev
            prev = curr1
            curr1 = nextt
        # ------------------------------------------ DONE------------------
        beg = prev
        curr2 = prev
        ele = 1 
        back = None
        while curr2:
            if ele == 1 and n==1:
                beg = curr2.next
                break
            if ele == n:
                back.next =curr2.next
                break
            ele+=1
            back = curr2
            curr2 = curr2.next
                
        # ------------------------------------------ SECOND REVERSING------------------
        prev_old = None
        while beg:
            lenn+=1
            nextt =beg.next
            beg.next =prev_old
            prev_old = beg
            beg= nextt

        return prev_old
        

        




            
        

        