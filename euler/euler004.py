# -*- coding: utf-8 -*- 
'''
A palindromic number reads the same both ways. The largest palindrome
made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit
numbers.
'''

import sys
import string
import os



def reverseNumber(num):
    cent=int(num/100)
    dec=int(int(num%100)/10)
    uni=int(num%10)
    return (uni*100) + (dec*10) + cent


def isPalindrome(num):
    part1=int(num/1000)
    part2=int(num%1000)
    rpart2=reverseNumber(part2)
    return part1==rpart2


def main():

    biggest=0

    for i in range(1,999):
        for j in range (1,999):
            num=i*j
            if isPalindrome(num):
                if (num>biggest):
                    biggest=num

    print (biggest)
    
    
    
    





if (__name__=='__main__'):
    main()
