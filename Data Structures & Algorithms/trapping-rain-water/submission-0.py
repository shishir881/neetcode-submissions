class Solution:
    def trap(self, height: List[int]) -> int:
        left_max=0
        left=0
        right_max=0
        right=len(height)-1
        water=0
        while left<right:
            if height[left]>=height[right]:

                if height[right]>right_max:
                    right_max=height[right]
                else:
                    h=right_max-height[right]
                    water+=h
                right-=1
            else:
                if height[left]>left_max:
                    left_max=height[left]
                else:
                    h=left_max-height[left]
                    water+=h
                left+=1
        return water

        