class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total = sum(cardPoints)
        n = len(cardPoints)
        maxx = 0
        taken = 0
        l = 0
        fix = n-k
        track = 0
        summ = 0
        for r in range(len(cardPoints)):
            summ+=cardPoints[r]
            track+=1
            while track>fix:
                summ-=cardPoints[l]
                track-=1
                l+=1
    
            if track==fix:
                maxx = max(maxx,total-summ)
        return maxx






        