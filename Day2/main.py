import sys
import math
from copy import deepcopy
from collections import defaultdict
from itertools import pairwise

input = open("Day2/input.txt").readlines()
input = [s.rstrip() for s in input]


def part1():
  safe = []
  for line in input:
    parsed = [int(x) for x in line.split()]

    good = check_line(parsed)

    if good:
      safe.append(parsed)

  #print(safe)
  print(len(safe))

def check_line(line):
  if line != sorted(line) and line != sorted(line, reverse=True):
    return False

  for c, n in pairwise(line):
    diff = abs(c - n)

    if diff > 3 or diff == 0:
      return False

  return True

def part2():
  safe = []
  for line in input:
    parsed = [int(x) for x in line.split()]

    good = False
    for i in range(len(parsed)):
      good = check_line(parsed[:i] + parsed[i+1:])
      if good:
        break

    if good:
      #int(parsed)
      safe.append(parsed)
  
  print(len(safe))

    

    
part1()
part2()