
num = int(input())
soma = [int(0)]*2001

for i in range(num): 
    x = int(input())
    soma[x] += 1

for i in range(2001):
    if (soma[i] > 0):
        print(f'{i} aparece {soma[i]} vez(es)') 