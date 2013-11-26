# -*- coding: utf-8 -*- 
'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can
see that the 6th prime is 13.

What is the 10 001st prime number?

'''

import sys

def isPrime(x,primes):
    for i in primes:
        if ((x%i)==0):
            return False
    return True


def main():
    
    primes=[2]
    i=3
    p=0
    while(len(primes)<10001):
        if (isPrime(i,primes)):
            primes.append(i)
        i+=1

    print (primes[len(primes)-1])






if (__name__=='__main__'):
    main()
