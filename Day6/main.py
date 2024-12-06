import sys
import math
from copy import deepcopy
from collections import defaultdict
from itertools import pairwise, permutations
import re

input = open("Day6/input.txt").readlines()
input = [s.rstrip() for s in input]

def find_start():
  for row in range(len(input)):
    for col in range(len(input[0])):
      if input[row][col] == '^':
        return (row,col)
      

DIRECTIONS = [(-1, 0), (0,1), (1, 0), (0, -1)]
input = [list(row) for row in input]

  
def part1():
  seen = set()
  (currentRow, currentCol) = find_start()
  directionIndex = 0
  grid = input
  while True:
    seen.add((currentRow, currentCol))

    dr, dc = DIRECTIONS[directionIndex]
    rr = currentRow + dr
    cc = currentCol + dc
  
    if not (0 <= rr < len(input) and 0 <= cc < len(input[0])):
      break

    if grid[rr][cc] == '#' or grid[rr][cc] == 'O':
      directionIndex = (directionIndex + 1) % 4
    else:
      currentRow = rr
      currentCol = cc
    
    #print(currentRow, currentCol, DIRECTIONS[directionIndex])


  print(len(seen))

def part2():
  loops = 0
  
  for row in range(len(input)):
    for col in range(len(input[0])):
      (currentRow, currentCol) = find_start()
      if row == currentRow and col == currentCol:
        continue

      grid = deepcopy(input)
      
      grid[row][col] = "O"
      seen = set()
      
      directionIndex = 0
      while True:
        if (currentRow, currentCol, directionIndex) in seen:
          loops += 1
          break
        seen.add((currentRow, currentCol, directionIndex))

        dr, dc = DIRECTIONS[directionIndex]
        rr = currentRow + dr
        cc = currentCol + dc
      
        if not (0 <= rr < len(input) and 0 <= cc < len(input[0])):
          break

        if grid[rr][cc] == '#' or grid[rr][cc] == 'O':
          directionIndex = (directionIndex + 1) % 4
        else:
          currentRow = rr
          currentCol = cc
        
        
    
    #print(currentRow, currentCol, DIRECTIONS[directionIndex])

  print(loops)

part1()
part2() #1482