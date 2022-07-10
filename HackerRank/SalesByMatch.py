
import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    list = []
    counter = 0
    for i in ar:
        if i not in list:
            list.append(i)
        else:
            counter += 1
            list.remove(i)
    return counter

print(sockMerchant(10,[1,2,3,2,2,3,3,2]))
