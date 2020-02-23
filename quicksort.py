from typing import List
from random import randint
def quicksort(A: List) -> None:
  if len(A) < 2:
    return A
  pivot_index = randint(0, len(A)-1)



