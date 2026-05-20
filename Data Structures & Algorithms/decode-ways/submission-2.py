class Solution:
    def numDecodings(self, s: str) -> int:
        cache={len(s):1}
        def memoization(i):
            if i in cache:
                return cache[i]
            if s[i]=="0":
                return 0
            res=memoization(i+1)
            if i<len(s)-1 and (s[i]=="1" or (s[i]=="2" and '0'<=s[i+1]<='6')):
                res+=memoization(i+2)
            cache[i]=res
            return res
        return memoization(0)
