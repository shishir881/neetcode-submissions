class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        right=len(heights)-1
        maxm=0
        while left<right:
            height=(right-left)*(min(heights[left],heights[right]))
            if height>maxm:
                maxm=height
            if heights[left]<heights[right]:
                left+=1
            elif heights[right]<heights[left]:
                right-=1
            else:
                left+=1
                right-=1
        return maxm
        