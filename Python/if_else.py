#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    # if n is odd print Weird
    if n%2 > 0:
        print("Weird")
    # if n is even
    else:
        # and if it between 2 and 5 print Not Weird
        if n >= 2 and n <= 5:
            print("Not Weird")
        # and if it between 6 and 20 print Weird
        elif n >= 6 and n <= 20:
            print("Weird")
        # and if it greater then 20 print Not Weird
        elif n > 20:
            print("Not Weird")

#Python If-Else
############################################################
#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
#Odd = Weird
#Even between 2 to 5 is Not Weird
#Even > 20 = Not Weird
#Even 6 to 20 = Weird
if (n%2  == 0 and 2 <= n < 6 )or(n%2 == 0 and n > 20) :
    print("Not Weird")
else:
    print("Weird") 
############################################################
