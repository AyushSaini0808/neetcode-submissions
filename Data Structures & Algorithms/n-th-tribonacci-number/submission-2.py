class Solution:
    def tribonacci(self, n: int) -> int:
        cache={}
        def dfs(i):
            if i<=2:
                return 1 if i!=0 else 0
            if i in cache:
                return cache[i]
            cache[i]=dfs(i-1)+dfs(i-2)+dfs(i-3)
            return cache[i]
        return dfs(n)