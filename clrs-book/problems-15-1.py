#!/usr/bin/python
# -*- coding: utf-8 -*- 


import string


longestPrefix=""

def esPalindromo(word):
    n=len(word)-1
    i=0
    while(n>=0):
        if word[i]!=word[n]:
            return False
        i+=1
        n-=1
    return True


def buscaPalindromo(word,prefix,level):
    global longestPrefix

    if (level>=len(word)-1):
        return
    else:
        print prefix
        if (esPalindromo(prefix)):
            if len(prefix)>=len(longestPrefix):
                longestPrefix=prefix

        c=level+1
        while (c<len(word)):
            prefix2=prefix+word[c]
            buscaPalindromo(word,prefix2,c)
            c+=1
        

def main():
    word="character"
    buscaPalindromo(word,"c",1)
    print "--->"+longestPrefix





if (__name__=='__main__'):
    main()
