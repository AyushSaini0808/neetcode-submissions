class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num2map={}
        for i, n in enumerate(nums2):
            num2map[n]=i
        mapping =[]
        for k in nums1:
            if k in num2map:
                mapping.append(num2map[k])
        return mapping