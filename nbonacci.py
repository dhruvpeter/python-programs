def nbonacci(n,m):
    list =[]
    cur_sum = 1
    for i in range(n-1):
        list.append(0)
        print("0",end = " ")
    list.append(1)
    print("1",end=" ")
    for i in range(n,m):
        list.append(cur_sum)
        print(cur_sum,end=" ")
        cur_sum+=cur_sum - list[i-n]

nbonacci(4,10)
