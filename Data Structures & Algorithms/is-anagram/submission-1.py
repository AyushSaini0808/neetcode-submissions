class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        sCountMap=Counter(s)
        tCountMap=Counter(t)
        for i in s:
            if i not in tCountMap or tCountMap[i]!=sCountMap[i]:
                return False
        return True