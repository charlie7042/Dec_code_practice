def sumN(n): # sum of all natural number till n
    if n == 1 or n==0:
        return 1
    else:        
        return n+sumN(n-1)
print(sumN(50))