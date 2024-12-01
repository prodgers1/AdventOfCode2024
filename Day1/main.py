import sys
import math
from collections import defaultdict

input = open("Day1/input.txt").readlines()
input = [s.rstrip() for s in input]


def parse():
  left = []
  right = []
  right_count = defaultdict(int)
  for line in input:
    l, r = line.split()
    left.append(l)
    right.append(r)
    right_count[r] += 1

  left = sorted(left)
  right = sorted(right)

  return left, right, right_count

def part1():
  left, right, _ = parse()
  total = 0

  for i, v in enumerate(left):
    l = left[i]
    r = right[i]

    distance = abs(int(l) - int(r))
    total += distance
  return total

def part2():
  left, right, right_count = parse()
  total = 0
  for i, v in enumerate(left):
    l = left[i]

    count = 0
    if l in right_count:
      count = right_count[l]
    
    similarity = int(l) * count
    total += int(similarity)

  return total


print(part1())
print(part2())