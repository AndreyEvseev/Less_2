def sum_number(n):
    m = n.replace('.', '')
    m = m.replace(',', '')
    m = m.replace('-', '')
    m = m.replace(' ', '')
    num = int(m)
    sum = 0
    while num != 0:
        sum = sum + num % 10
        num //= 10
    return sum

n = input('Введите вещественное число: ')
sum = sum_number(n)
print(sum)
