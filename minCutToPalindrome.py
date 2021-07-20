def min_cut(input,l,r):
    first = l
    last = r
    while(input[first]==input[last]):
        first +=1
        last -=1
        if first >= last:
            return 0
    return 1 + min(min_cut(input,l+1,r),min_cut(input,l,r-1))
    
input = "abbaaba"
print(min_cut(input,0,len(input)-1))