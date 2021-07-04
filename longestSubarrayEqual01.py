def longestSubarrayWithEqual0sAnd1s(arr, n):
    curSum = arr[0]
    curLength = 1

    maxLength = 0
    for i in range(1, n):
        if curLength % 2 == 0 and curLength // 2 == curSum:
            maxLength = max(maxLength, curLength)
        else:

#incomplete
