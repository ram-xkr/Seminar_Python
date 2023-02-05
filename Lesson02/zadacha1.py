n = int(input('Введите количество арбузов: '))
min = 1000
max = 0
for i in range(n):
    massa = int(input('Введите вес арбуза: '))
    if max < massa:
        max = massa
    else:
        if min > massa:
            min = massa
print(min, max)