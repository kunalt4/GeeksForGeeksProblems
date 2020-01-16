#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    res = [0] * (n+1)
    maxVal = 0
    runSum = 0
    for start,end,val in queries:
        res[start-1]+=val
        res[end]-=val
    
    for i in range(len(res)):
        runSum+=res[i]

        if runSum>maxVal:
            maxVal = runSum
    return maxVal


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
