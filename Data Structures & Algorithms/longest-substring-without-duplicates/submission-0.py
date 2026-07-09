class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen=set()
        left=0
        right=0
        max_len=0
        for i in range(len(s)):
            curr=s[i]
            while curr in seen:
                seen.remove(s[left])
                left+=1
            seen.add(curr)
            right=i

            l=right-left+1
            if l>max_len:
                max_len=l
        return max_len
            


        