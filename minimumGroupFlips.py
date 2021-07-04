#Mininumum number of group flips to make all elements same in binary array

#if start and end group is same, that group is more, so flip the second group
#if start and end is same, both groups have same number, so any group can be flipped

#flipping 2nd groups

def flip(list,n):
    for i in range(1,n):
        if list[i] != list[i-1]:
            if list[i] != list[0]:
                print("From ",i,end = " ")
            else:
                print("to ",i-1)
    if list[n-1] != list[i]:
        print("to ",n-1)


list = [1,0,0,0,1,0,0,1,1,1,1]
flip(list,len(list))

            