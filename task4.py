# Дружественные числа

def func(n):
    sum_mult = 0
    for k in range(1, n // 2 + 1):
        if n % k == 0:
            sum_mult += k
    return sum_mult


n = int(input("Введите число: "))
for i in range(1, n):
    # num_1 = func(i)
    # for j in range(i + 1, n):
    #     num_2 = func(j)
    #     if(num_1 == j and num_2 == i):
    #         print(i, j)
    j = func(i)
    t = func(j)
    if (i == t and i < j):
        print(i, j)