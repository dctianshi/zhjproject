#coding: utf-8

def hanoi(n,X,Y,Z):
    if (n==1):
        print(X,'-->',Z)
        return
    hanoi(n-1,X,Z,Y)
    print(X,'-->',Z)
    hanoi(n-1,Y,X,Z)
hanoi(5,'A','B','C')
