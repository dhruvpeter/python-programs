n=int(input("Enter a number: "))
num = n
sum = 0
while(num>0):
    r = num%10
    num=num//10
    sum+=r**3
    print(sum)
if sum == n:
    print(n,"is an armstrong number")
else:
    print(n,"is not an armstrong number")
print(15/2)