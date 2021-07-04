import math
N=5
M=2
arr = [5,10]
arr.sort()
no_of_dealer = [0]*M
i = M-1
miss_count = 0
prev_N = N
while N > 0:
    if arr[i]>no_of_dealer[i]:
        N-=1
        no_of_dealer[i]+=1
    if prev_N == N:
        miss_count+=1
    else:
        prev_N = N
        miss_count = 0
    if miss_count == M:
        break
    i = i-1 if i!=0 else M-1
max_jealousy = 0
for i in range(M):
    max_jealousy = max(max_jealousy,math.ceil(arr[i]/no_of_dealer[i]))
print(max_jealousy)