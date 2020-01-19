#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.
from itertools import combinations
def sherlockAndAnagrams(s):
    count = 0
    for i in range(1,len(s)):
        j = 0
        a = []
        while j < (len(s)-i+1):
            a.append(s[j:j+i])
            j = j+1
        i = i+1
        for a,c in combinations(a,2):
            if sorted(a) == sorted(c):
                count+=1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
