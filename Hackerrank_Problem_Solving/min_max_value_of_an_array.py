# Given five positive integers, find the minimum and maximum values that can be
# calculated by summing exactly four of the five integers. 
# Then print the respective minimum and maximum values as a single line of two 
# space-separated long integers.


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    arr=(sorted(arr))
    min_sum = 0
    max_sum =0 
    for j in range(len(arr)-1):
        min_sum += arr[j]
    for j in range(1,len(arr)):
        max_sum += arr[j]
    print(min_sum, max_sum , end=' ')

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

          