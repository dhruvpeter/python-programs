def freqSorted(list):
    count = 1
    for i in range(1,len(list)):
        if list[i] == list[i-1]:
            count += 1
        else:
            print(list[i-1],count)
            count = 1
    print(list[len(list)-1],count)

list = []
i= int(input())
while i!= -1:
    list.append(i)
    i=int(input())
freqSorted(list)