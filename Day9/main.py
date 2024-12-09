import sys
import math
from copy import deepcopy
from collections import defaultdict
from itertools import pairwise, permutations, product
import re

input = open("Day9/input.txt").readlines()
input = [s.rstrip() for s in input][0]

def create_disk():
  id = 0
  disk = []
  free_spaces = []
  id_disk_map = defaultdict(int)
  
  for i, block in enumerate(input):
    if i % 2 == 0:
      for j in range(int(block)):
        disk.append(id)
      id_disk_map[id] = int(block)
      id += 1
    else:
      current_free = []
      start = len(disk)
      for j in range(int(block)):
        disk.append('')
        current_free.append(start)
        start += 1
      if current_free:
        free_spaces.append(current_free)
    
  return disk, free_spaces, id_disk_map

def shift_left(disk):
  while disk.count('') > 0:
    empty = [i for i, v in enumerate(disk) if v == '']
    
    for empty_space in empty:
      if disk.count('') == 0:
        break

      to_move = disk.pop()
      if to_move == '':
        break
      
      disk[empty_space] = to_move
  
  return disk

def shift_left_2(disk, free_spaces, id_disk_map):
  file_to_move = max(id_disk_map.keys())
  free_space_index = 0
  used = []
  while free_space_index < len(free_spaces):
    changed = False
    for id in reversed(id_disk_map.keys()):
      if id in used:
        continue
      file_size = id_disk_map[id]
      open = free_spaces[free_space_index]

      if file_size <= len(open) and disk.index(id) > open[0]:
        changed = True
        to_remove = disk.index(id)
        for i in range(file_size):
          disk[to_remove+i] = ''


        used.append(id)
        for i in range(file_size):
          disk[open[i]] = id
          
        
        for i in range(file_size):
          del free_spaces[free_space_index][0]
      
      if len(free_spaces[free_space_index]) == 0:
        free_space_index += 1
    if not changed:
      free_space_index += 1


  #print(free_spaces)
  #print(disk)
  return disk


def calculate_check_sum(disk):
  check_sum = 0
  for i, v in enumerate(disk):
    if v == '':
      continue
    check_sum += (i * v)
  return check_sum

disk, free_spaces, id_disk_map = create_disk()
#disk = shift_left(disk)
shift_left_2(disk, free_spaces, id_disk_map)
#print(id_disk_map)
#print(disk)
print(calculate_check_sum(disk))
