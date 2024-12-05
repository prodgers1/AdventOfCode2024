import sys
import math
from copy import deepcopy
from collections import defaultdict
from itertools import pairwise, permutations
import re

input = open("Day6/input.txt").readlines()
input = [s.rstrip() for s in input]