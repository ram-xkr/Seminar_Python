n = int(input('Введите количество монеток: '))
orel = 0
reshka = 0
for i in range(n):
    a = int(input('Введите 0 или 1:'))
    if a == 1:
        orel += 1
    else:
        reshka += 1
if orel < reshka:
    print(orel)
else:
    print(reshka)