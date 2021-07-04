def towerOfHanoi(n,A,B,C):
    if n==1:
        print("Move 1 from",A,"to",C)
        return
    towerOfHanoi(n-1,A,C,B)
    print("Move",n,"from",A,"to",C)
    towerOfHanoi(n-1,B,A,C)

n=int(input())
towerOfHanoi(n,'A','B','C')