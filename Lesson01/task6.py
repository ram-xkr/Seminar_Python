ticket = int(input())
a = ticket // 100000 + (ticket // 10000) % 10 + (ticket // 1000) % 10
b = (ticket // 100) % 10 + (ticket // 10) % 10 + ticket % 10
if a == b:
    print('yes')
else:
    print('no')