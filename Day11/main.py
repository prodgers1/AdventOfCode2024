from functools import lru_cache
import sys
import math
from copy import deepcopy
from collections import defaultdict
from itertools import pairwise, permutations, product
import re

input = open("Day11/input.txt").readlines()
input = [s.rstrip() for s in input][0]

# pretty much copied from JP, bottom is my part 1 and attempt at memoization

def is_stone_zero(stone):
  return int(stone) == 0

def is_stone_even_digits(stone):
  if len(str(stone)) % 2 == 0:
    index = len(str(stone)) // 2

    start = int(str(stone)[:index])
    end = int(str(stone)[index:])

    return start, end
  return None, None

def multiply_stone(stone):
  return int(stone) * 2024


DP = {}

def solve(stone, times):
  if (stone, times) in DP:
    return DP[(stone, times)]
  
  if times == 0:
    r = 1
  elif is_stone_zero(stone):
    r = solve(1, times-1)
  elif len(str(stone)) % 2 == 0:
    start, end = is_stone_even_digits(stone)
    r = solve(start, times-1) + solve(end, times-1)
  else:
    r = solve(stone*2024, times-1)
  
  DP[(stone, times)] = r
  return r

def blink(stones, times):
  return sum(solve(int(s), times) for s in stones.split())


print(blink(input, 25))
print(blink(input, 75))

  # DP = {}
  # new_arrangement = input.split()
  # for i in range(75):
  #   print(i)
  #   arrangement = new_arrangement
  #   new_arrangement = []
    
  #   for stone in arrangement:
  #     stone = int(stone)
  #     if stone in DP:
  #       new_arrangement.extend(DP[stone])
  #       continue

  #     result = []

  #     if is_stone_zero(stone):
  #       result.append(1)
  #     else:
  #       start, end = is_stone_even_digits(stone)
  #       if start is not None and end is not None:
  #         result.append(start)
  #         result.append(end)
  #       else:
  #         result.append(multiply_stone(stone))

  #     DP[stone] = result
  #     new_arrangement.extend(result)
  #   #print(new_arrangement)

  # print(len(new_arrangement))
