def paarissumma(n):
    if n < 2:
        return 0
    elif n % 2 == 0:
        return n + paarissumma(n - 2)
    else:
        return paarissumma(n - 1)


print(paarissumma(1))  
print(paarissumma(10)) 
print(paarissumma(11)) 
