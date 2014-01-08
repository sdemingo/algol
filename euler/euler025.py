'''
Problem 25

The 12th term, F12, is the first term to contain three digits.

What is the first term in the Fibonacci sequence to contain 1000
digits?  
'''


def fib(n):
    a, b = 0,1
    z=1
    for i in range(n):
        a, b = b, a + b
        z+=1
        if len(str(b))>=1000:
            print (z)
            return


def main():
    fib(10000)
 






if (__name__=='__main__'):
    main()
