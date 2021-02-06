import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    x = list()
    for i in arr[::-1]:
        x.append(str(i))
    a = " ".join(x)
    print(a)