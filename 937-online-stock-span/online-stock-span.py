class StockSpanner:

    def __init__(self):
        self.stack = []
        self.time = 1 
    
    def next(self, price: int) -> int:
        self.time+=1
        if not self.stack:
            self.stack.append((price,self.time))
            return 1
        else:
            while self.stack and self.stack[-1][0]<= price:
                self.stack.pop()
            if not self.stack:
                self.stack.append((price,self.time))
                return self.time-1


            if self.stack:
                val,tme = self.stack[-1]
                self.stack.append((price,self.time))
                return self.time - tme

            self.stack.append((price,self.time))


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)