# Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
# разобраться в его кричалках не настолько просто, насколько легко он их
# придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть,
# если число слогов (т.е. число гласных букв) в каждой фразе стихотворения
# одинаковое. Фраза может состоять из одного слова, если во фразе несколько
# слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами.
# Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе напишите
# “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом
# все не в порядке
# Ввод:                                       Вывод:
# пара-ра-рам рам-пам-папам па-ра-па-дам      Парам пам-пам

stih = "пара-ра-рам рам-пам-папам па-ра-па-дам"
glasnye = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
frazy = stih.split()

count = []

for i in frazy:
    cnt = 0
    for j in i:
        if j.lower() in glasnye:
            cnt += 1
    count.append(cnt)
print(count)

if count.count(count[0]) == len(count):
    print('Парам пам-пам')
else:
    print('Пам парам')


