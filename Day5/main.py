import sys
import math
from copy import deepcopy
from collections import defaultdict
from itertools import pairwise, permutations
import re

input = open("Day5/input.txt").readlines()
input = [s.rstrip() for s in input]

ordering_rules = defaultdict(list)
updates = list()

for rule in input:
  if '|' in rule:
    l, r = rule.split('|')   
    ordering_rules[int(l)].append(int(r))
  elif ',' in rule:
    updates.append([int(x) for x in rule.split(',')])

seen = set()

def page_in_order(update):
  for i, page in enumerate(update):
   rest = update[i+1:]
   
   for r in rest:
     if r not in ordering_rules[page]:
      return False
  
  return True

def print_ans(l):
  ans = 0
  for good in l:
    middle = good[len(good) // 2]
    ans += middle
  return ans


def page_in_order_2(update):
  for i, page in enumerate(update):
   rest = update[i+1:]
   
   for r in rest:
     if r not in ordering_rules[page]:
      return False, i
  
  return True, None


in_order = list()
not_in_order = list()
not_in_order_now_in_order = list()

# part 1
for update in updates:
  if page_in_order(update):
    in_order.append(update)
  else:
    not_in_order.append(update)

# part 2
for notGood in not_in_order:
  current = notGood[:]
  while True:
   good, indexOfBad = page_in_order_2(current)
   if good:
     not_in_order_now_in_order.append(current)
     break
   bad_page = current[indexOfBad]
   for i in range(indexOfBad + 1, len(current)):
    if bad_page in ordering_rules[current[i]]:
      current[indexOfBad], current[i] = current[i], current[indexOfBad]
      break

print(print_ans(in_order))
print(print_ans(not_in_order_now_in_order))