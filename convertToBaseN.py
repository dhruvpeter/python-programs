def convertToBaseN(list,number,n):
    if number == 0:
        return
    else:
        convertToBaseN(list,int(number//n),n)
        list.append(str(number%n))


number = int(input())
n = int(input())
list=[]
convertToBaseN(list,number,n)
print(''.join(list))