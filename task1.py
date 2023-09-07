# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
# Ввод: Вывод:
# 7 3 3 2 12
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1

def func(my_list, yours_list):
    answer = list()
    for value in my_list:
        if value not in yours_list:
            answer.append(value)
    return answer

def generation(m):
    my_list = list()
    for i in range(m):
        value = int(input("Введите элемент первого множества: "))
        my_list.append(value)
    return my_list

m = int(input("Введите количество элементов первого множества: "))
my_list = generation(m)

k = int(input("Введите количество элементов второго множества: "))
yours_list = generation(k)

print(func(my_list, yours_list))