"""
ID: kqanto1
LANG: PYTHON3
TASK: milk
"""
m = []
sum = 0
with open('milk.in','r') as f:
    a = list(map(int,f.readline().split()))
    cost = a[0]
    n = a[1]
    for i in range(n):
        m.append(list(map(int,f.readline().split())))
    m.sort()

for i in range(len(m)):
    if m[i][1] < cost:
        cost -= m[i][1]
        sum += m[i][0]*m[i][1]
    else:
        sum += cost*m[i][0]
        break
    print(cost,sum)

with open('milk.out','w+') as f:
    f.write(f'{sum}\n')