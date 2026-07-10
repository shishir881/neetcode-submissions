class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        max_n=0
        for right in range(len(s)):
            l=right-left+1
            rem = l-(Counter(s[left:right+1]).most_common(1)[0][1])
            if rem <=k and l>max_n:
                max_n=l
            elif rem>k:
                left+=1
        return max_n


