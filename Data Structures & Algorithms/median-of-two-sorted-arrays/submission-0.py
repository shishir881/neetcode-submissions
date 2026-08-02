class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        l=0
        r=len(nums1)
        m1=r
        m2=len(nums2)
        while l<=r:
            i=(l+r)//2
            j=((m1+m2+1)//2)-i

            left1 = nums1[i - 1] if i > 0 else float('-inf')
            right1 = nums1[i] if i < m1 else float('inf')
            
            left2 = nums2[j - 1] if j > 0 else float('-inf')
            right2 = nums2[j] if j < m2 else float('inf')

            if left1>right2:
                r=i-1
            elif left2>right1:
                l=i+1
            else:
                if (m1+m2)%2==0:
                    return (max(left1,left2) + min(right1,right2)) / 2
                else:
                    return max(left1,left2)
            

