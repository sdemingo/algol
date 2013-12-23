'''
Problem 24

A permutation is an ordered arrangement of objects. For example, 3124
is one possible permutation of the digits 1, 2, 3 and 4. If all of the
permutations are listed numerically or alphabetically, we call it
lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2,
3, 4, 5, 6, 7, 8 and 9?
'''



def perm(lista):
    if (len(lista)==2):
        return [[lista[0],lista[1]],[lista[1],lista[0]]]
    else:
        ap=[]
        for e in lista:
            copia=lista[:]
            primero=e
            copia.remove(e)
            for p in perm(copia):
                ap.append([primero]+p)

        return ap



def main():
    a=perm([0,1,2,3,4,5,6,7,8,9])
    a.sort()
    print ("".join(map(str,a[999999])))

    






if (__name__=='__main__'):
    main()
