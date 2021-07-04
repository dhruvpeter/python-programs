def makeSubsets(s,n,i,sub):
    if i==n:
        print(sub)
    if i<n:
        makeSubsets(s,n,i+1,sub)
        makeSubsets(s,n,i+1,sub+s[i])

s= input()
makeSubsets(s,len(s),0,"")