#Factorial N

n = int(input("Insert N: "))
#n = 5
fact = 1 
for i in range(1,n+1):
    fact = fact * i 

print(f'Factorial N: {fact}')