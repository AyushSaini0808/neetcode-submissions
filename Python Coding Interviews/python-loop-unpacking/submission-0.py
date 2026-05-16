from typing import List, Tuple


def best_student(scores: List[Tuple[str, int]]) -> str:
    highest=0
    hname=""
    for name,mark in scores:
        x,y=name,mark
        if y>highest:
            highest = y
            hname=x
    return hname


# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))
