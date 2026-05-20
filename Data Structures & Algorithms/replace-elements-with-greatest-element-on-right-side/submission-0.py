class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_int=arr[-1]
        arr[-1]=-1
        for i in range(len(arr)-2,-1,-1):
            if max_int<arr[i]:
                temp=max_int
                max_int=arr[i]
                arr[i]=temp
                continue
            arr[i]=max_int
        return arr