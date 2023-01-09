#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input().strip())
    if N%2 > 0:
        print("Weird")
    elif N%2 == 0:
        if 2 >= N or N <= 5:
            print("Not Weird")
        elif 6 >= N or N <= 20:
            print("Weird")
        elif N > 20:
            print("Not Weird")
