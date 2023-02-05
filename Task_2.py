def set_products(n):
    set_prod = [1]
    if n < 1:
        for i in range(0, n - 1, -1):
            set_prod.append(set_prod[-1] * i)
    else:
        for j in range(2, n + 1):
            set_prod.append(set_prod[-1] * j)
    return set_prod

n = int(input('Введите натуральное число: '))
set_prod = set_products(n)
print(set_prod)