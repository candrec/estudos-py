def collatz(number):
    if (number % 2) == 0:
        return number // 2
    else:
        return 3 * number + 1

num = int(input('Digite um inteiro:\n'))

while True:
    num = collatz(num)
    print(num)
    if num == 1:
        break