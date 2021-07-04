def permutation(l,n,perm):
    if n == 0:
        res = ""
        res = res.join(perm)
        print(res)
        return

    for i in range(len(l)):
        elem = l[i]
        l.pop(i)
        permutation(l,n-1,perm+[elem])
        l.insert(i,elem)
    

s= input()
l= [char for char in s]
permutation(l,len(l),[])