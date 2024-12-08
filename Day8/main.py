import sys
import math
from copy import deepcopy
from collections import defaultdict
from itertools import pairwise, permutations, product
import re

input = open("Day8/input.txt").readlines()
input = [s.rstrip() for s in input]
input = [list(row) for row in input]

antennas = defaultdict(list)

for row in range(len(input)):
  for col in range(len(input[0])):
    if input[row][col] != '.':
      antennas[input[row][col]].append((row, col))


movements = []
for key, antenna in antennas.items():
  #print(antenna)
  for i in range(len(antenna)):
    for j in range(i+1 ,len(antenna)):
      current = antenna[i]
      n = antenna[j]
      drow = n[0] - current[0]
      dcol = n[1] - current[1]
      movements.append((current, n, (drow, dcol)))

#print(movements)

def print_ans(antinodes, debug=False):
  if debug:
    for antinode in antinodes:
      print("".join(antinode))

  ans = 0
  for row in range(len(antinodes)):
    for col in range(len(antinodes[0])):
      if antinodes[row][col] == '#':
        ans += 1
  print(ans)

def part1():
  antinodes = deepcopy(input)
  for start, end, (drow, dcol) in movements: 
    for dr, dc in [(drow, dcol), (-drow, -dcol)]:
      currentRow = start[0]
      currentCol = start[1]
      while True:
        currentRow = currentRow + dr
        currentCol = currentCol + dc

        if (currentRow, currentCol) == end:
          continue

        if not( 0 <= currentRow < len(input) and 0 <= currentCol < len(input[0])):
          break
        antinodes[currentRow][currentCol] = '#'
        break
  print_ans(antinodes)
  
def part2():
  antinodes = deepcopy(input)
  for start, end, (drow, dcol) in movements: 
    for dr, dc in [(drow, dcol), (-drow, -dcol)]:
      currentRow = start[0]
      currentCol = start[1]
      while True:
        # for some reason all antennas turn into antinodes
        if antinodes[currentRow][currentCol] != '#':
          antinodes[currentRow][currentCol] = '#'

        currentRow = currentRow + dr
        currentCol = currentCol + dc

        if not( 0 <= currentRow < len(input) and 0 <= currentCol < len(input[0])):
          break
        antinodes[currentRow][currentCol] = '#'
        #break #go the full length of the grid not just one step
  print_ans(antinodes)

antinodes = part1()
antinodes = part2()