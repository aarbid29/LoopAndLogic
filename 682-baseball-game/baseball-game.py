class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op == "C":
                stack.pop()
            elif op == "D":
                doubl = (stack[-1])*2
                stack.append(doubl)
            elif op=="+":
                top = stack[-1]
                top2 = stack[-2]
                add = top + top2
                stack.append(add)
            else:
                stack.append(int(op))
    
        return sum(stack)


        