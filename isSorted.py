def isSorted(l):
    for i in range(1,len(l)):
        if l[i] < l[i-1]:
            return False
    return True



list = []
i= int(input())
while i!= -1:
    list.append(i)
    i=int(input())
print(isSorted(list))