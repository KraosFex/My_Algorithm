#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    return " ".join([s.split(" ")[i].capitalize() for i in range(len(s.split(" ")))])

if __name__ == '__main__':
    ## fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = solve(s)
    print(result)
    # fptr.write(result + '\n')
    # fptr.close()
