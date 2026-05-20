class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_int=-1
        for i in range(len(arr)-1,-1,-1):
            temp=max_int
            max_int = max(max_int,arr[i])
            arr[i]=temp
        return arr