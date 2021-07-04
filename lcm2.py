n1 = int(input("Enter a number: "))
n2 = int(input("Enter another number: "))
l=max(n1,n2)
m=min(n1,n2)
val = l
i=2
while val%m != 0:
    val = l * i
    i+=1
print("\n",val)