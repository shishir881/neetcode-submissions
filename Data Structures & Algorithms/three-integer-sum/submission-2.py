class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        snum=sorted(nums)
        result=[]
        n=len(nums)
        for i in range(n):
            if i>0 and snum[i]==snum[i-1]:
                continue
            j=i+1
            k=n-1
            while j<k:
                if snum[j]+snum[k]>(-snum[i]):
                    k-=1
                elif snum[j]+snum[k]<(-snum[i]):
                    j+=1
                elif snum[j]+snum[k]==(-snum[i]):
                    result.append([snum[i],snum[j],snum[k]])
                    while j<k and snum[j]==snum[j+1]:
                        j+=1
                    while j<k and snum[k]==snum[k-1]:
                        k-=1
                    
                    j+=1
                    k-=1
        return result


        