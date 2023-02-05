from math import sqrt
s, p = int(input()), int(input())
z = sqrt((s/2)**2 - p)
print(int(s/2 - z), int(s/2 + z))

