n1 = int(input("Enter a number: "))
n2 = int(input("Enter another number: "))
if n1 < n2:
    num = n1
else:
    num = n2
while (num>=1):
    if((n1%num==0)and(n2%num==0)):
        break
    num-=1
print("HCF(%d,%d) : %d"%(n1,n2,num))