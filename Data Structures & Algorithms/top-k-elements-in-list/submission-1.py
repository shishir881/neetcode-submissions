class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        n=len(nums)
        result=[]
        buckets = [[] for _ in range(n + 1)]
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        for elem,rate in freq.items():
            buckets[rate].append(elem)
        for i in range(len(buckets) - 1,0,-1):
            if buckets[i]:
                for num in buckets[i]:
                    result.append(num)
                    if len(result)==k:
                        return result
            
            

        