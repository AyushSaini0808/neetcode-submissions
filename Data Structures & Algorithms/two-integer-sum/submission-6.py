class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dMap={}
        for i,n in enumerate(nums):
            diff=target-n
            if diff in dMap:
                return [dMap[diff],i]
            dMap[n]=i
