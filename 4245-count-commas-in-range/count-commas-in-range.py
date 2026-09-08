class Solution:
    def countCommas(self, n: int) -> int:
        st = str(n)
        nn = len(st) -1 

        if len(st)<4:
            return 0
        if len(st) ==4:
            return n-999

        
        # for 1 2 3 4   5 

        #step 1 : for curr digit 5  , 1 -> 4 zeros , 10,000 - 12345 = 2345 + 1

        #  step 2 :for 4 digit , max is 9999 - 1000 -> plus 1

        #step 1 :
        maxx = 10**nn
        diff = n- maxx + 1
        #step 2 :
        min_nine = 1000
        max_nine = 10**nn - 1
        diff2 = max_nine - min_nine + 1
        # max_nine = int(strr)
        # ntow = nn-1
        # ss = "1"+ "0"*ntow
        # maxx_ten = int(ss)

        # maxx_ten = 10**(ntow)
        # diff2 = max_nine - maxx_ten + 1 

        return diff+ diff2

         



        
        

        

        

        
                    

        