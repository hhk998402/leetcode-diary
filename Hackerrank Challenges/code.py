'''
https://www.hackerrank.com/challenges/one-week-preparation-kit-plus-minus/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-one
'''

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
    neg,zero,pos,n = 0.0,0.0,0.0,len(arr)
    for i in arr:
        if(i < 0):
            neg+=1
        elif(i>0):
            pos+=1
        else:
            zero+=1
    print("{:.6f}".format(round(pos/n, 6)))
    print("{:.6f}".format(round(neg/n, 6)))
    print("{:.6f}".format(round(zero/n, 6)))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
