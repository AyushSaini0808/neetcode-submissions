class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroCount=0
        maxProduct=1
        for i in nums:
            if i==0:
                zeroCount+=1
                if zeroCount==2:
                    return [0]*len(nums)
                continue
            maxProduct*=i
        for i in range(len(nums)):
            if zeroCount==0:
                nums[i]=maxProduct//nums[i]
            else:
                if nums[i]!=0:
                    nums[i]=0
                else:
                    nums[i]=maxProduct
        return nums
        
            