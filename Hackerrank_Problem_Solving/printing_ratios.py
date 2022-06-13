#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    pos = 0
    neg = 0
    zero = 0
    for element in arr:
        if (element==0):
            zero += 1
        elif (element>0):
            pos += 1
        else:
            neg += 1
    lenght= len(arr)
    
    print(round((pos/lenght),6))
    print(round((neg/lenght),6))
    print(round((zero/lenght),6))
   

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
