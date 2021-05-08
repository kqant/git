"""
ID: kqanto1
LANG: PYTHON3
TASK: milk2
"""

milk = []
with open('milk2.in', 'r') as f:
    n = int(f.readline())
    for i in range(n):
        milk.append(list(map(int,f.readline().split())))
milk.sort()
fin = 0
start = milk[0][0]
ost = milk[0][1] - milk[0][0]
timing = 0
max1 = milk[0][1]
for i in range(len(milk)):
    if fin < milk[i][0]:
        if milk[i][0] - fin > timing and i > 1:
            timing = milk[i][0] - fin
        start = milk[i][0]
        fin = milk[i][1]
    if milk[i][1] > fin:
        fin = milk[i][1]
    if fin - start > ost:
        ost = fin-start

with open('milk2.out', 'w') as f:
    f.write(f"{ost} {timing}\n")
