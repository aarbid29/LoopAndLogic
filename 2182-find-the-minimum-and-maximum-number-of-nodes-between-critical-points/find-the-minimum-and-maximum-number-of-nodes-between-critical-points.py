class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:

        curr = head.next
        prev = head
        stack = []
        i = 2

        while curr.next:

            if curr.val < prev.val and curr.val < curr.next.val:
                stack.append(i)

            if curr.val > prev.val and curr.val > curr.next.val:
                stack.append(i)

            i += 1
            prev = curr
            curr = curr.next

        if len(stack) < 2:
            return [-1, -1]

        mindistance = float('inf')

        for i in range(1, len(stack)):
            mindistance = min(mindistance, stack[i] - stack[i - 1])

        maxdistance = stack[-1] - stack[0]

        return [mindistance, maxdistance]