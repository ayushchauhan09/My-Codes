import math
import os
import random
import re
import sys

def dayOfProgrammer(year):
    if year <= 1917:
        if year%4 == 0:
            return f"{256-244}.09.{year}"
        else:
            return f"{256-243}.09.{year}"
    elif year == 1918:
        return f"{256-230}.09.{year}"
    else:
        if year%400 == 0 or (year%4 ==0 and year%100 !=0):
            return f"{256-244}.09.{year}"
        else:
            return f"{256-243}.09.{year}"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
