import time as t


startTime = t.time()
for num in range(1,10_000):
    isPrime = True
    divCount = 0
    for div in range(1,num):
        if(num%div==0):
            divCount+=1
        if(divCount>=2):
            isPrime = False
            break
    if isPrime :
        print(num,end=" ")
myTime = t.time() - startTime
print("\n\n")
# eratisthenis method
primeList = []
numbers = []
for i in range(2,10000):
    numbers.append(i)
    
startTime = t.time()
while(len(numbers)):
    num = numbers[0]
    numbers.remove(num)
    primeList.append(num) 
    for i in numbers:
        if i % num == 0:
            numbers.remove(i)
print(primeList)
print(f'\n\nMy Method took :{myTime}s')
print(f'Eratosthenis Method took: {t.time() - startTime}s\n\n')