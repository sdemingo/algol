'''
Problem 30

Surprisingly there are only three numbers that can be written as the
sum of fourth powers of their digits:

    1634 = 14 + 64 + 34 + 44
    8208 = 84 + 24 + 04 + 84
    9474 = 94 + 44 + 74 + 44

As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of
fifth powers of their digits.
'''


def splitNumber(num):
    
    n=num
    digits=[]
    while (n>0):
        digit=n%10
        digits.append(digit)
        n=n//10

    digits.sort()
    return digits



def main():

    nums=[]
    for number in range(2,1000000):
        digits=splitNumber(number)
        total=0
        l=0
        for d in digits:
            total+=d**5
            l+=1
            if (total>=number):
                break

        if ((total==number) and (l==len(digits))):
            nums.append(number)

    print (nums)
    print (sum(nums))




if (__name__=='__main__'):
    main()
