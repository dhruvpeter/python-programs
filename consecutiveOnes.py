def maxConsecutiveOnes(arr,n):
    maxcount = 0
    count = 0
    for i in range(n):
        if arr[i] == 1:
            count += 1
        else:
            maxcount = max(maxcount , count)
            count = 0
    return maxcount

list = [1,1,1,0,0,1,1,1,1,1,0,0]
print(maxConsecutiveOnes(list,len(list)))