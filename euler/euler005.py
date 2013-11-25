# -*- coding: utf-8 -*- 
'''
2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all
of the numbers from 1 to 20?
'''

import sys
import string
import os
import functools

# mcm: Mínimo Común Múltiplo (lcm or  least common multiple in English)
# mcd: Máximo Común Divisor (gcd or greatest common divisor in English)

def mcm(a,b):
    mcd, tmp = a,b
    while tmp != 0:
        mcd,tmp = tmp, mcd % tmp
    return a*b/mcd


def main():
    print(functools.reduce(mcm, range(1,21)))
 


if (__name__=='__main__'):
    main()
