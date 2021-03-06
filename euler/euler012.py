'''
The sequence of triangle numbers is generated by adding the natural
numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7
= 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

     1: 1
     3: 1,3
     6: 1,2,3,6
    10: 1,2,5,10
    15: 1,3,5,15
    21: 1,3,7,21
    28: 1,2,4,7,14,28

We can see that 28 is the first triangle number to have over five
divisors.

What is the value of the first triangle number to have over five
hundred divisors?
'''

import math

#
# Método de búsqueda de divisores clásico. No eficiente. Para números
# con más de cinco divisores funciona, para números con más de 500 no. 
#

def divisors1(n):
    i=1
    for i in range(1,n//2+1):
        if (n%i)==0:
            yield i
    yield n

#
# Método de búsqueda de divisores más eficiente. Funciona para números
# grandes con más de 500 divisores. Sacado de:
# http://stackoverflow.com/a/171779
#
# Busca los divisores por parejas. Para cada divisor pequeño encontrado
# (i) que puede oscilar entre el 1 y el siguiente a la raíz de n,
# buscamos su pareja. Cada divisor pequeño tendra una pareja en divisor
# grande que sea n/i. Ej: 28 tiene como divisor pequeño a 4 y como
# divisor grande a 28/4=7

def divisors2(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i is 0:
            yield i
            if i is not n / i:
                large_divisors.insert(0, n / i)

    for divisor in large_divisors:
        yield divisor


def main():

    i=0
    t=0
    while (True):
        i+=1
        t=t+i
        l=len(list(divisors2(t)))
        if l>500: break

    print (t)




if (__name__=='__main__'):
    main()
