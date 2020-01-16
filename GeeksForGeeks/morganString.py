#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the morganAndString function below.
def morganAndString(a, b):
    result = []
    temp = []
    list_a = list(a)
    list_b = list(b)

    list_a.reverse()
    list_b.reverse()
    print(list_b)
    print(list_a)
    i = 0 
    while(list_a and list_b and i<min(len(list_a),len(list_b))):   
        if list_a[-1] < list_b[-1]:
            result.append(list_a.pop())
        elif list_a[-1] > list_b[-1]:
            result.append(list_b.pop())
        elif list_a[-1] == list_b[-1]:
            while(list_a[-1] == list_b[-1]):
                temp.append(list_a.pop())
                print(result)
            if list_a[-1] < list_b[-1]:
                list_b.append(temp)
            else:
                list_a.append(temp)
            i = i+1
    if(list_a):
        list_a.reverse()
        result.extend(list_a)
    elif(list_b):
        list_b.reverse()
        result.extend(list_b)
    print("".join(result))
    return "".join(result)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        a = input()

        b = input()

        result = morganAndString(a, b)

        # fptr.write(result + '\n')

    # fptr.close()
