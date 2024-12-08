import sys
import math
from copy import deepcopy
from collections import defaultdict
from itertools import pairwise, permutations, product
import re

input = open("Day9/input.txt").readlines()
input = [s.rstrip() for s in input]