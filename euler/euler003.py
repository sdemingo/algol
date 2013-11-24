# -*- coding: utf-8 -*- 
'''
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''

import sys
import string
import os


def isPrime(x):
    for i in range(2,int(x/2)):
        if ((x%i)==0):
            return False
    return True

def main():
    
    num=600851475143
    largest=0
    i=2

    while (i<=num):
        if ((num%i)==0):
            num=int(num/i)
            if (isPrime(i)):
                largest=i
        i+=1

    print (largest)





if (__name__=='__main__'):
    main()
