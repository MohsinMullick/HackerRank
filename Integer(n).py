"""Task
Given an integer, , perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than , print Not Weird
Input Format

A single line containing a positive integer, ."""

#!/bin/python3

import math
import os
import random
import re
import sys


if __name__=="__main__":
    n=int(input().strip())
    if n%2!=0:
        print(f"Weird")
    else:
        if 2<=n<=5:
            print(f"Not Weird")
        else:
            if 6<=n<=20:
                print(f"Not Weird")
            else:
                if n>20:
                    print(f"Not Weird")


