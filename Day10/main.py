import sys
import math
from copy import deepcopy
from collections import defaultdict
from itertools import pairwise, permutations, product
import re

input = open("Day10/input.txt").readlines()
input = [s.rstrip() for s in input]

start = set()
for row in range(len(input)):
  for col in range(len(input[0])):
    if input[row][col] == '0':
      start.add((row, col))

#print(start)

# UP, Right, Down, Left
DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
def dfs(row, col, currentLevel, visited, peaks):  
  if (row,col) in visited:
    return 0
  visited.add((row, col))

  trails = 0
  if input[row][col] == '9':
    peaks.add((row,col))
    visited.remove((row, col))
    return 1
  
  for dr, dc in DIRECTIONS:
    rr = row + dr
    cc = col + dc
    if not (0 <= rr < len(input) and 0 <= cc < len(input[0])):
      continue

    if input[rr][cc] == '.':
      continue

    if int(input[rr][cc]) == (currentLevel + 1):
      trails += dfs(rr, cc, currentLevel + 1, visited, peaks)
  
  visited.remove((row, col))
  return trails

trails_p1 = 0
trails_p2 = 0
for s in start:
  visited = set()
  peaks = set()
  trails_p2 += dfs(s[0], s[1], 0, visited, peaks)
  trails_p1 += len(peaks)
  
print(trails_p1)
print(trails_p2)
