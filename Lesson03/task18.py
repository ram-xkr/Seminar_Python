# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5

n = int(input('Введите количество элементов: '))
x = int(input('Введите число: '))
list = []
print(n)

for i in range(1, n + 1):
    list.append(i)
print(list)
print(x)

if x > max(list):
    print(list[-1])
elif x < min(list):
    print(list[0])
else:
    print(x)
