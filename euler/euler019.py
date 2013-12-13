'''
Problem 19

You are given the following information, but you may prefer to do some research for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

'''


months=[0,31,28,31,30,31,30,31,31,30,31,30,31]
week=["L","M","X","J","V","S","D"]


def isLeap(year):
    if (year % 4 == 0 and not year % 100 == 0) or year % 400 == 0:
        return True
    else:
        return False




def countSundays(year,firstDay):
    s=firstDay
    sundays=0

    if (s==6):    # Si el primer dia del año es domingo, incremento
        print ("El 1/1 fue "+week[s])
        sundays+=1

    for m in range(1,12):
        f=(s+months[m])%7
        if (f==6):
            print ("El 1/"+str(m+1)+" fue "+week[f])
            sundays+=1

        s+=months[m]
        if (isLeap(year) and (m==2)):
            s+=1 #uno mas a febrero por ser bisiesto

    return sundays





def main():
    suns=1
    s=1 # 1 Por el martes de 1/1/1901
    for y in range(1901,2001):
        first=s%7
        print ("Año: "+str(y)+":")
        d=countSundays(y,first)
        suns+=d
        print ("\t\t\t domingos: "+str(d)+" suns: "+str(suns))
        s+=365
        if isLeap(y):
            s+=1
        
    print (suns)






if (__name__=='__main__'):
    main()
