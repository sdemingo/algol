'''
Problem 17

If the numbers 1 to 5 are written out in words: one, two, three, four,
five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were
written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred
and forty-two) contains 23 letters and 115 (one hundred and fifteen)
contains 20 letters. The use of "and" when writing out numbers is in
compliance with British usage.
'''

numbers1=[""]*10
numbers1[1]="one"
numbers1[2]="two"
numbers1[3]="three"
numbers1[4]="four"
numbers1[5]="five"
numbers1[6]="six"
numbers1[7]="seven"
numbers1[8]="eight"
numbers1[9]="nine"

numbers2=[""]*10
numbers2[0]="ten"
numbers2[1]="eleven"
numbers2[2]="twelve"
numbers2[3]="thirteen"
numbers2[4]="fourteen"
numbers2[5]="fifteen"
numbers2[6]="sixteen"
numbers2[7]="seventeen"
numbers2[8]="eighteen"
numbers2[9]="nineteen"

numbers3=[""]*10
numbers3[1]="ten"
numbers3[2]="twenty"
numbers3[3]="thirty"
numbers3[4]="forty"
numbers3[5]="fifty"
numbers3[6]="sixty"
numbers3[7]="seventy"
numbers3[8]="eighty"
numbers3[9]="ninety"


def number2words(n):
    if (n<10):  #0-9
        return numbers1[n]

    if (n<20):  #10-19
        return numbers2[n%10]
    
    if (n<100): #20-99
        d=n//10
        r=n%10
        return numbers3[d]+" "+numbers1[r]
      
    if (n<1000): #100-999
        c=n//100
        r=n%100
        rs=number2words(r)
        if (rs!=""):
            return numbers1[c]+" hundred and "+rs
        else:
            return numbers1[c]+" hundred"
    
    return ""


def main():
    n=0
    for i in range(1,1000):
        r=number2words(i)
        n+=len(r.replace(" ",""))

    n+=len("onethousand")
    print (n)








if (__name__=='__main__'):
    main()
