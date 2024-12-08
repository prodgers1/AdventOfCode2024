import sys
import math
from copy import deepcopy
from collections import defaultdict
from itertools import pairwise, permutations, product
import re

input = open("Day7/input.txt").readlines()
input = [s.rstrip() for s in input]

true_expressions = []
for equation in input:
  answer, numbers = equation.split(': ')
  numbers = [int(x) for x in numbers.split()]
  #print(answer, numbers)

  number_of_operators = len(numbers) - 1
  OPERATORS = ['*', '+', '||']
  
  operators_to_try = list(product(OPERATORS, repeat=number_of_operators))
  expressions = []

  for operators in operators_to_try:
    expression = str(numbers[0])
    result = 0
    for number, operator in zip(numbers[1:], operators):
      if operator == '||':
        expression = f"{expression}{number}"
      else:
        expression += f" {operator} {number}"
        result = eval(expression)
        expression = str(result)
    expressions.append(expression)
  
  
  for ans in expressions:
    if int(ans) == int(answer):
      true_expressions.append(answer)
      break
  
print(len(true_expressions))
print(sum([int(x) for x in true_expressions]))
    