def josuphus(n,k,list,i,count,killed):
    if killed == n-1:
        for i in range(n):
            if list[i]==1:
                print(i)
                return
    if list[i]!=0:
        if count == k-1:
            list[i]=0
            return josuphus(n,k,list,(i+1)%n,0,killed+1)
        else:
            return josuphus(n,k,list,(i+1)%n,count+1,killed)
    elif list[i]==0:
        return josuphus(n,k,list,(i+1)%n,count,killed)
n=int(input())
k=int(input())
list=[1]*n
josuphus(n,k,list,0,0,0)
#print(res)