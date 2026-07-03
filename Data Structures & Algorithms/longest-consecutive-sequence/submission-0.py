class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        arr=set()
        for i in range(len(nums)):
            arr.add(nums[i])
        max=0
        for i in range(len(nums)):
            curr=nums[i]
            if curr-1 in arr:
                continue
            else:
                j=0
                while True:
                    if curr+j in arr:
                        j+=1
                    else:
                        if j>max:
                            max=j
                        break
        return max                




            
