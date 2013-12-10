'''
* Problem 4.1-3 of CLRS. Pág 74

The brute-force rutine for solving the maximum-subarray problem in an
integer vector.
'''

import random
import time


def findMaxCrossing(v,lw,md,hg):
    left_sum=-1000000
    sum=0
    max_left=0
    max_right=0
    for i in reversed(range(lw,md+1)):
        sum+=v[i]
        if sum>left_sum:
            left_sum=sum
            max_left=i

    right_sum=-1000000
    sum=0
    for j in range(md+1,hg+1):
        sum+=v[j]
        if sum>right_sum:
            right_sum=sum
            max_right=j
    return (max_left, max_right, left_sum + right_sum)



def findMaximumSubArray(v,lw,hg):
    
    if lw==hg:
        return (lw,hg,v[lw])     # Base Case
    else:
        mid=(lw+hg)//2
           
        (left_low,left_high,left_sum)=findMaximumSubArray(v,lw,mid)
        (right_low,right_high,right_sum)=findMaximumSubArray(v,mid+1,hg)
        (cross_low,cross_high,cross_sum)=findMaxCrossing(v,lw,mid,hg)

        if (left_sum>=right_sum) and (left_sum>=cross_sum):
            return (left_low,left_high,left_sum)
        elif (right_sum>=left_sum) and (right_sum >= cross_sum):
            return (right_low,right_high,right_sum)
        else:
            return (cross_low,cross_high,cross_sum)




def recursive(v):
    return findMaximumSubArray(v,0,len(v)-1)



def forcebrute(v):
    max=-1000000
    r=len(v)
    l=0
    for i in range(len(v)):
        sum=0
        for j in range(i,len(v)):
            sum+=v[j]
            if (sum>=max):
                max=sum
                r=j
                l=i
    return (l,r,max)




def main():
    v=[random.randint(-9,9) for i in range(5000)]

    start = time.time()
    left,right,value=forcebrute(v)
    end = time.time()
    print ("Bruteforce: left={0} right={1} value={2} in {3:.8f} secs".format(left,right,value, end-start))

    start = time.time()
    left,right,value=recursive(v)
    end = time.time()
    print ("Recursive:  left={0} right={1} value={2} in {3:.8f} secs".format(left,right,value, end-start))




if (__name__=='__main__'):
    main()
