def maxAmazingTriplets(a,n):
    if n<3:
        return -1
    ans = 0
    for j in range(1,n-1):
        maxi = a[j-1]
        for i in range(0,j):
            if a[i]<a[j]:
                maxi = max(maxi,a[i])
        maxk = a[j+1]
        for k in range(j+1,n):
            if a[i]<a[k]:
                maxk = max(maxk,a[k])
        ans = max(ans,maxi + a[j] * maxk)
    return ans


a = [16,18,19,17]
ans = maxAmazingTriplets(a,len(a))
print(ans)