def countSubset(list,n,i,sub,sum):
    if i==n:
        s = 0
        for el in sub:
            s+=el
        if s == sum:
            return 1
        else:
            return 0
    return countSubset(list,n,i+1,sub,sum) + countSubset(list,n,i+1,sub+[list[i]],sum)

list = []
i= int(input())
while i!= -1:
    list.append(i)
    i=int(input())
sum = int(input())
count = countSubset(list,len(list),0,[],sum)
print(count)