class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        l=len(s1)
        left=0
        num=[0]*26
        slide=[0]*26
        for i in range(l):
            num[ord(s1[i])-ord("a")]+=1
            slide[ord(s2[i])-ord("a")]+=1
        if num==slide:
            return True

        for i in range(l,len(s2)):
            slide[ord(s2[i-l])-ord("a")]-=1
            slide[ord(s2[i])-ord("a")]+=1
            if num==slide:
                return True
        return False



        