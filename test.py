str=input("Enter string: ")
f=0
i=0
j=len(str)-1
while (i<j):
   if(str[i]==str[j]):
      i+=1
      j-=1
      continue
   else:
      print("Not a palindrome")
      f=1
      break12
if f==0:
   print("Palindrome")