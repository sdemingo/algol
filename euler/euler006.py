# -*- coding: utf-8 -*- 
'''
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 102 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten
natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one
hundred natural numbers and the square of the sum.
'''

import sys
import string
import os


def main():
    
    sq=0
    for i in range(1,101):
        sq=sq+(i*i)

    qs=0
    for i in range(1,101):
        qs=qs+i

    qs=qs*qs

    dif=qs-sq
    print (dif)




if (__name__=='__main__'):
    main()
