i = input().split(' ')
x, y, n = i
x = int(x)
y = int(y)
n = int(n)

for num in n:
    if num % x == 0 and num % y == 0:
        print('FizzBuzz')
    elif num % x == 0:
        print('Fizz')
    elif num % y == 0:
        print('Buzz')
    else:
        print(num)
