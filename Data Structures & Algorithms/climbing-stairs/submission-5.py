class Solution:
    def climbStairs(self, n: int) -> int:
        cache=[-1]*n
        def memoization(i):
            if i>=n:
                return i==n
            if cache[i]!=-1:
                return cache[i]
            cache[i]=memoization(i+1)+memoization(i+2)
            return cache[i]
        return memoization(0)
