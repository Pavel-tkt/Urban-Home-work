numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
Prime = []
NotPrime = []
for i in range(2,len(numbers)) :
    isPrime =True
    for j in range(2,int(i** 0.5) + 1):
        if i % j == 0:
            isPrime = False
            break
        isPrime = True
    if isPrime:
        Prime.extend([i])
    else:
        NotPrime.append(i)
print('Prime:', (Prime))
print('NotPrime:', (NotPrime))