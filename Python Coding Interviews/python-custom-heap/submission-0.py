import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    max_heap=[]
    for i in range(len(nums)):
        pair = (-nums[i],nums[i])
        heapq.heappush(max_heap,pair)

    res=[]
    for i in range(len(nums)):
        pair=heapq.heappop(max_heap)
        res.append(pair[1])
    return res




# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
