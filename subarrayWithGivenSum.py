def subarrayExist(a,n,sum):
    curSum = a[0]
    begin = 0
    if curSum == sum:
        return True
    i = 1
    while i < n:
        if curSum == sum:
            return True
        elif curSum < sum:
            curSum += a[i]
            i += 1
        else:
            curSum -= a[begin]
            begin += 1
    return False

list = [1,4,20,3,10,5]
sum = 33
print(subarrayExist(list,len(list),sum))