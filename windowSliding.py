def maximumSum(arr,n,k):
    maxSum = 0
    for i in range(k):
        maxSum += arr[i]
    curSum = maxSum
    for i in range(k,n):
        curSum = curSum - arr[i-k] + arr[i]
        maxSum = max(maxSum,curSum)
    return maxSum
       
arr = [5,-10,6,90,3]
k = 2
print(maximumSum(arr,len(arr),k))