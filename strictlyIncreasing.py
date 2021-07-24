def strictlyIncreasing(a,n):
    a[0] = 0
    for i in range(1,n):
        if a[i] > a[i-1]:
            a[i] = a[i-1] + 1
        else:
            return "No"
    return "Yes"

    #Alternate solution
    #--------------
    # for i in range(n):
    #     if a[i] < i:
    #         return "No"
    # return "Yes"


a = [5,20,15,10]
print(strictlyIncreasing(a,len(a)))