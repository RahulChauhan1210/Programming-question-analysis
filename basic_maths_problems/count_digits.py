def countDigit( n):
        count = 0
        if n is None:
            return count 
        else :
            while n > 0:
              count += 1
              n //= 10    
        return count  


print(countDigit(100))