def sum_number(n):
    m = n.replace('.', '').replace(',', '').replace('-', '').replace(' ', '')
    num = int(m)
    summa = 0
    while num != 0:
        summa = summa + num % 10
        num //= 10
    return summa

n = input('Введите вещественное число: ')
sum_digit = sum_number(n)
print(sum_digit)
