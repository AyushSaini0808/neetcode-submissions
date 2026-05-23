class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter=Counter(nums)
        q=[]
        for n,v in counter.items():
            pair=(-v,n)
            heapq.heappush(q,pair)
        res=[]
        for i in range(k):
            res.append(heapq.heappop(q)[1])
        return res
