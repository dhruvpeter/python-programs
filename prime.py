n=100
for num in range(1,n+1):
    f=0
    if num==1:
        continue
    for i in range(2,num):
        if num%i == 0:
            f=1
            break
    if f==0:
        print(num)
