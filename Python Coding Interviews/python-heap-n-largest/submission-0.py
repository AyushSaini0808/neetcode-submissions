import heapq
from typing import List


def get_max_element(arr: List[int]) -> int:
    arr=[-a for a in arr]
    heapq.heapify(arr)
    return -1*heapq.heappop(arr)


def get_max_4_elements(arr: List[int]) -> List[int]:
    # Return elements in *decreasing* order
    arr=[-a for a in arr]
    res=[]
    for i in range(4):
        heapq.heapify(arr)
        res.append(-1*heapq.heappop(arr))
    return res

def get_max_2_elements(arr: List[int]) -> List[int]:
    # Return elements in *increasing* order
    arr=[-a for a in arr]
    res=[]
    for i in range(2):
        heapq.heapify(arr)
        res.append(-1*heapq.heappop(arr))
    return res[::-1]


# do not modify below this line
print(get_max_element([1, 2, 3]))
print(get_max_element([3, 2, 1, 4, 6, 2]))
print(get_max_element([1, 9, 7, 3, 2, 1, 4, 6, 2]))

print(get_max_4_elements([4, 9, 7, 3, 2, 7, 4, 6, 2]))
print(get_max_4_elements([4, 9, 7, 2, 1, 3, 2, 3, 4, 6, 2, 3]))
print(get_max_4_elements([4, 7, 2, 3, 2, 4, 6, 2]))

print(get_max_2_elements([4, 5, 3, 7]))
print(get_max_2_elements([8, 8, 7, 9]))
print(get_max_2_elements([1, 2, 3, 9, 8, 7, 6]))

