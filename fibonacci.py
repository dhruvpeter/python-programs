f1=0
f2=1
n=int(input("No. of terms: "))
i=0
print(f1)
print(f2)
i+=2
while(i<n):
    temp=f2
    f2+=f1
    f1=temp
    print(f2)
    i+=1