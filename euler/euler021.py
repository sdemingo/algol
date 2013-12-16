''' 
Problem 21

Let d(n) be defined as the sum of proper divisors of n (numbers
less than n which divide evenly into n).  If d(a) = b and d(b) = a,
where a ? b, then a and b are an amicable pair and each of a and b are
called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20,
22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284
are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''

import math



#
# Función para calcular divisores sacada de euler012.py
#

def divisors(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i is 0:
            yield i
            if i is not n / i:
                large_divisors.insert(0, n / i)

    for divisor in large_divisors:
        yield divisor


def main():
    
    m=[0 for i in range(0,100000)]
    friendly=[]

    for i in range(2,10000):
        n=int(sum(list(divisors(i))))-i
        m[i]=n
        if (m[n]!=0) and ( (m[i]==n) and (m[n]==i) and (n!=i)):
            if n not in friendly:
                friendly.append(n)
            if i not in friendly:
                friendly.append(i)

    print (sum(friendly))
  





if (__name__=='__main__'):
    main()
