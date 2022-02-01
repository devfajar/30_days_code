# Day 28 regex and patterns and intro to db
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    name = []
    N = int(input().strip())

    for N_itr in range(N):
        first_multiple_input = input().rstrip().split()

        firstName = first_multiple_input[0]

        emailID = first_multiple_input[1]
        if emailID[-10:] == "@gmail.com":
            name.append(firstName)

    name = sorted(name)
    for item in name:
        print(item)
