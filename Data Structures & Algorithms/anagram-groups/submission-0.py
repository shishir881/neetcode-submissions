class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group={}
        final=[]
        for word in strs:
            sort="".join(sorted(word))
            if sort in group:
                group[sort].append(word)
            else:
                group[sort]=[word]
        for value in group:
            value_list=group[value]
            final.append(value_list)
        return final