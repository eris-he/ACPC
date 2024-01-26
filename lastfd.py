from math import factorial
n = int(input())
for _ in range(n):
    print(factorial(int(input())) % 10)