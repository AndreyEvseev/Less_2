def sum_number(n):
    m = str(n).replace('.', '')
    m = str(m).replace(',', '')
    m = str(m).replace('-', '')
    m = str(m).replace(' ', '')
    num = int(m)
    sum = 0
    while num != 0:
        sum = sum + num % 10
        num //= 10
    return sum

n = float(input('Введите вещественное число: '))
sum = sum_number(n)
print(sum)


