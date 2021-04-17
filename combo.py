from itertools import *
"""
ID: kqanto1
LANG: PYTHON3
TASK: combo
"""
otv = []
c = 0
with open('combo.in','r') as f:
    n = f.readline().split()
    n = int(n[0])
    d = list(map(int,f.readline().split()))
    d1 = list(map(int, f.readline().split()))
numbers = [],[],[]
numbers1 = [],[],[]
for i in range(3):
    numbers[i].append(d[i])
    numbers1[i].append(d1[i])
    if d[i] + 1 <= n:
        numbers[i].append(d[i]+1)
    elif 1 <= d[i] + 1 - n <= n:
        numbers[i].append(d[i] + 1 - n)
    if d[i] + 2 <= n:
        numbers[i].append(d[i]+2)
    elif 1 <= d[i] + 2 - n <= n:
        numbers[i].append(d[i] + 2 - n)
    if d[i] - 1 >= 1:
        numbers[i].append(d[i]-1)
    elif 1 <= n+d[i]-1 <= n:
        numbers[i].append(n+d[i]-1)
    if d[i] - 2 >= 1:
        numbers[i].append(d[i] - 2)
    elif 1 <= n + d[i] - 2 <= n:
        numbers[i].append(n + d[i] - 2)
    if d1[i] + 1 <= n:
        numbers1[i].append(d1[i]+1)
    elif 1 <= d1[i] + 1 - n <= n:
        numbers1[i].append(d1[i] + 1 - n)
    if d1[i] + 2 <= n:
        numbers1[i].append(d1[i]+2)
    elif 1 <= d1[i] + 2 - n <= n:
        numbers1[i].append(d1[i] + 2 - n)
    if d1[i] - 1 >= 1:
        numbers1[i].append(d1[i]-1)
    elif 1 <= n + d1[i] - 1 <= n:
        numbers1[i].append(n+d1[i]-1)
    if d1[i] - 2 >= 1:
        numbers1[i].append(d1[i] - 2)
    elif 1 <= n + d1[i] - 2 <= n:
        numbers1[i].append(n + d1[i] - 2)
numbers = list(numbers)
numbers1 = list(numbers1)

pr = product(numbers[0],numbers[1],numbers[2])
pr1 = product(numbers1[0],numbers1[1],numbers1[2])
for x in pr:
    if not(x in otv):
        c += 1
        otv.append(x)
for x in pr1:
    if not(x in otv):
        c += 1
        otv.append(x)
print(otv)
f = open('combo.out','w+')
f.write(f'{c}\n')


