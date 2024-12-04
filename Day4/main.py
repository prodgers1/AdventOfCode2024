import sys
import math
from copy import deepcopy
from collections import defaultdict
from itertools import pairwise
import re

input = open("Day4/input.txt").readlines()
input = [s.rstrip() for s in input]

def in_range(row, col):
  return 0 <= row < len(input) and 0 <= col < len(input[0])

def dfs(row, col, index, drow, dcol, word):
  if index == len(word):
    return True
  elif not in_range(row, col) or input[row][col] != word[index]:
    return False
  
  return dfs(row + drow, col + dcol, index + 1, drow, dcol)

def find_xmas():
  DR = [-1, 0, 1]
  DC = [-1, 0, 1]
  WORD = "XMAS"
  count = 0
  for row in range(len(input)):
    for col in range(len(input[0])):
      if input[row][col] == 'X':
        for drow in DR:
          for dcol in DC:
            valid = dfs(row, col, 0, drow, dcol, WORD)

            if valid:
              count += 1

  return count

def is_x_mas(row, col):
  DR = [-1, 1]
  DC = [-1, 1]

  rowBoundary = 0 <= row - 1 < len(input) and 0 <= row + 1 < len(input)
  colBoundary = 0 <= col - 1 < len(input[0]) and 0 <= col + 1 < len(input[0])

  if not rowBoundary or not colBoundary:
    return False
  # M   S
  #   A
  # M   S

  topLeftValid = input[row - 1][col - 1] == 'M'
  topRight = input[row-1][col + 1] == 'S'
  currentValid = input[row][col] == 'A'
  bottomLeftValid = input[row+1][col-1] == 'M'
  botomRightValid = input[row+1][col+1] == 'S'

  # S   M
  #   A
  # S   M

  topLeftValid2 = input[row - 1][col - 1] == 'S'
  topRight2 = input[row-1][col + 1] == 'M'
  currentValid2 = input[row][col] == 'A'
  bottomLeftValid2 = input[row+1][col-1] == 'S'
  botomRightValid2 = input[row+1][col+1] == 'M'

  # M   M
  #   A
  # S   S
  topLeftValid3 = input[row - 1][col - 1] == 'M'
  topRight3 = input[row-1][col + 1] == 'M'
  currentValid3 = input[row][col] == 'A'
  bottomLeftValid3 = input[row+1][col-1] == 'S'
  botomRightValid3 = input[row+1][col+1] == 'S'

  # S   S
  #   A
  # M   M
  topLeftValid4 = input[row - 1][col - 1] == 'S'
  topRight4 = input[row-1][col + 1] == 'S'
  currentValid4 = input[row][col] == 'A'
  bottomLeftValid4 = input[row+1][col-1] == 'M'
  botomRightValid4 = input[row+1][col+1] == 'M'

  return ((topLeftValid and topRight and currentValid and bottomLeftValid and botomRightValid)
  or (topLeftValid2 and topRight2 and currentValid2 and bottomLeftValid2 and botomRightValid2)
  or (topLeftValid3 and topRight3 and currentValid3 and bottomLeftValid3 and botomRightValid3)
  or (topLeftValid4 and topRight4 and currentValid4 and bottomLeftValid4 and botomRightValid4))
  

def find_mas_in_x(): 
  count = 0
  for row in range(len(input)):
    for col in range(len(input[0])):
      if is_x_mas(row, col):
        count += 1

  return count

print(find_mas_in_x())