# -*- coding: utf-8 -*- 
'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
'''

import sys

# Criba de eratóstenes

def primes_sieve(limit):
    limitn = limit+1
    not_prime = set()
    primes = []

    for i in range(2, limitn):
        if i in not_prime:
            continue

        # Si sigo es que i es primo asi que:

        # meto a todos los multiplos de i hasta limitn en el conjunto 
        # de not_prime
        for f in range(i*2, limitn, i): 
            not_prime.add(f)

        # Lo añado a la lista de primos
        primes.append(i)

    return primes


def main():
    primes=primes_sieve(2000000)

    sum=0
    for i in primes:
        sum+=i

    print(sum)

    



if (__name__=='__main__'):
    main()
