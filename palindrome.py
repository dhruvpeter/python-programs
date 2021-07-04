def palindrome(s,n,k):
    if n==k or k==n+1:
        return True

    if s[n] == s[k]:
        return palindrome(s,n-1,k+1)
    else:
        return False

s= input()
print(palindrome(s,len(s)-1,0))