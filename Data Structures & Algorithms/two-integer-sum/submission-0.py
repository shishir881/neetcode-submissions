class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val={}
        for i in range(len(nums)):
            cur=nums[i]
            diff=target-cur
            if diff in val:
                return [val[diff],i]
            val[cur]=i

