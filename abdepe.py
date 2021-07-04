def abdepe(n):
    sum=0
    for i in range(1,n):
        if (n%i == 0):
            sum += i
    if(sum > n):
#        print("Abundant number")
        pass
    elif(sum<n):
        print(n)
#       print("Deficient number")
#    else:
#        print("Perfect number")

for i in range(1,25):
    abdepe(i)