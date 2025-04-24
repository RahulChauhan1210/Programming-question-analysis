def GCD(n1, n2):
    if n1 != n2:
        if n1>n2 :
            return GCD(n1-n2,n2)
        else:
           return GCD(n1,n2-n1)
    else:
        return n1

print(GCD(4,6))