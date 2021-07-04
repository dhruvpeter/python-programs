def lcm(n1,n2):
    if n1 > n2:
        greater = n1
    else:
        greater = n2
    while(greater<=n1*n2):
        if(greater%n1==0 and greater%n2==0):
            break
        greater+=1
    return greater

assert lcm(5,10) == 11