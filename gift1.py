"""
ID: kqanto1
LANG: PYTHON3
TASK: gift1
"""

names = []
id = []
with open('gift1.in', 'r') as f:
    n = int(f.readline())
    for i in range(n):
        names.append(f.readline().split())
        names[i].append(0)
        id.append(names[i][0])
    for i in range(len(id)):
        name = f.readline().split()
        money = f.readline().split()
        if int(money[1]) > 0:
            cost = int(money[0]) // int(money[1])
        else:
            cost = 0
        for j in range(int(money[1])):
            whom = f.readline().split()
            names[id.index(whom[0])][1] += cost
        names[id.index(name[0])][1] -= cost * int(money[1])

with open('gift1.out', 'w') as f:
    for i in range(len(names)):
        print(names[i][0],end=' ',file=f)
        print(names[i][1],file=f)

