
num1 = int(input())
num2 = int(input())

maior = num1 if num1 > num2 else num2
menor = num1 if num1 < num2 else num2

for num in range(menor+1, maior):
    if num % 5 == 2 or num % 5 == 3:
        print(num)