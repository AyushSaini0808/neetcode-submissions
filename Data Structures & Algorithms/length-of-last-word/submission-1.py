class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.strip()
        res=0
        i=len(s)-1
        while i>=0:
            if s[i]!=" ":
                res+=1
                i-=1
            else:
                break
        return res