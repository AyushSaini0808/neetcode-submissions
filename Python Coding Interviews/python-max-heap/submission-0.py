import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    nums=[-n for n in nums]
    res=[]
    for _ in range(len(nums)):
        heapq.heapify(nums)
        res.append(-1*heapq.heappop(nums))
    return res






# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
