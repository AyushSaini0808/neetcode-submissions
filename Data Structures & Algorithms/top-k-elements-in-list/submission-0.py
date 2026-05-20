class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        buckets=[0]*(n+1)
        counter=Counter(nums)
        for num,freq in counter.items():
            if buckets[freq]==0:
                buckets[freq]=[num]
            else:
                buckets[freq].append(num)
        res=[]
        for i in range(n,0,-1):
            if buckets[i]!=0:
                res.extend(buckets[i])
            if len(res)==k:
                return res
