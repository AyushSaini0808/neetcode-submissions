import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        q=[-val for val in stones]
        heapq.heapify(q)
        while q and len(q)!=1:
            x=heapq.heappop(q)
            y=heapq.heappop(q)
            if x!=y:
                heapq.heappush(q,-(abs(x-y)))
        return -q[0] if q else 0
