import functools
def number_of_ways(n: int, m: int) -> int:
  @functools.lru_cache(None)
  def compute_number_of_ways_to_xy(x, y):
    if x == y == 0:
      return 1
    ways_top = 0 if x == 0 else compute_number_of_ways_to_xy(x - 1, y)
    ways_left = 0 if y == 0 else compute_number_of_ways_to_xy(x, y - 1)
    return ways_top + ways_left
  
  return compute_number_of_ways_to_xy(n - 1, m - 1)

ans = number_of_ways(5, 5)
print(ans)
