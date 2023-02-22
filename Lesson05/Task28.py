# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух
# целых неотрицательных чисел.
# 2 2
# 4

def summa(a, b):
    if b == 0:
        return a
    return summa(a, b - 1) + 1


x = int(input("Введите первое число: "))
y = int(input("Введите второе число: "))
print(summa(x,y))