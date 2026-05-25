import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for i in nums:
            count[i]=1+count.get(i,0)
        q=[]
        for j,v in count.items():
            heapq.heappush(q,(-v,j))
        res=[]   
        for j in range(k): 
            res.append(heapq.heappop(q)[1])
        return res