def isArmstrong(n):
    o = n
    l = len(str(n))
    sum = 0
    for i in range(l):
        k = n%10
        n = n//10
        sum += k**l 
    if sum == o:
        return True
    return False
    
print(isArmstrong(153))  