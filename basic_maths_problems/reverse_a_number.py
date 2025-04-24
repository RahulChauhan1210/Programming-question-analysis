def reverseNumber(n):
    n = int(''.join(list(str(n))[::-1]))
    return n 
print(reverseNumber(10012))
