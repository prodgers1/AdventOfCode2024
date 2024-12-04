import sys
import math
from copy import deepcopy
from collections import defaultdict
from itertools import pairwise
import re

input = open("Day3/input.txt").read()
#input = [s.rstrip() for s in input]

pattern = r'mul\((\d*),(\d*)\)'
DONT = "don't()"
DO = "do()"

def find_ans(line):
  matches =  re.findall(pattern, line)
  ans = 0
  for match in matches:
    ans += (int(match[0]) * int(match[1]))
    #print(ans)
  return ans

print(find_ans(input))

ans = 0
enabled_memory = []
for match in re.split(r"do\(\)", input):
  index = match.find(DONT)
  if index != -1:
      enabled_memory.append(match[:index])
  else:
      enabled_memory.append(match)

test = "".join(enabled_memory)
ans += find_ans(test)

print(ans)
