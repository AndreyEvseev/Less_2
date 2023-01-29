def set_products(n):
    set = [1]
    if n < 1:
        for i in range(0, n - 1, -1):
            set.append(set[-1] * i)
    else:
        for j in range(2, n + 1):
            set.append(set[-1] * j)
    return set

n = int(input('Введите натуральное число: '))
set = set_products(n)
print(set)