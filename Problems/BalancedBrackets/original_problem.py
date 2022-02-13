#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'isBalanced' function below.


def isBalanced(s: str) -> str:
    pass
    # Write your code here


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + "\n")

    fptr.close()
