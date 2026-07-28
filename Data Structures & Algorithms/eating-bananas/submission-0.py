class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        u=max(piles)
        l=1
        min_k=u
        while l<u:
            k=(u+l)//2
            total=0
            for i in range(len(piles)):
                total+=math.ceil(piles[i]/k)
            if total<=h:
                u=k
            else:
                l=k+1
        return l