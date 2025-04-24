def isPalindrome(n):
    n = str(n)
    l = len(n)
    for i in range(int(l/2)):
        if n[i]!=n[-(i+1)]:
            return False
    return True    

print(isPalindrome(1011201))