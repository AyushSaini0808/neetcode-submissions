class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idxMap={}
        for i, n in enumerate(nums):
            idxMap[n]=i
        for i in range(len(nums)):
            diff=target - nums[i]
            if diff in idxMap and i!=idxMap[diff]:
                return [i,idxMap[diff]]

