class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idxMap={}
        for k in range(len(nums)):
            diff=target-nums[k]
            if diff in idxMap.keys():
                return [idxMap[diff],k]
            idxMap[nums[k]]=k
            