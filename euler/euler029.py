'''
Problem 29

'''


def main():
    
    numbers=[]
    for a in range(2,101):
        for b in range(2,101):
            n=a**b
            if n not in numbers:
                numbers.append(n)

    print (len(numbers))






if (__name__=='__main__'):
    main()
