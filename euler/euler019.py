'''
Problem 19
'''

months=[0,31,28,31,30,31,30,31,31,30,31,30,31]
week=["L","M","X","J","V","S","D"]


def isLeap(year):
    if (year % 4 == 0 and not year % 100 == 0) or year % 400 == 0:
        return True
    else:
        return False


# def firstDayOfMonths():
#     s=1  #primer dia del año fue martes (2)

#     print ("El 1/1 fue "+week[s])
#     for m in range(1,12):
#         f=(s+months[m])%7
#         s+=months[m]
#         print ("El 1/"+str(m+1)+" fue "+week[f])
    

def countSundays(year,firstDay):
    s=firstDay
    sundays=0

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
    suns=0
    s=1 # 1 Por el martes de 1/1/1901
    for y in range(1901,2001):
        first=s%7
        print ("Primer día del "+str(y)+" fue "+week[first])
        suns+=countSundays(y,first)
        s+=365
        if isLeap(y):
            s+=1
        
    print (suns)








if (__name__=='__main__'):
    main()
