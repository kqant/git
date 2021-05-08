"""
ID: kqanto1
LANG: PYTHON3
TASK: dualpal
"""
alphabet = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
with open('dualpal.in', 'r') as f:
    x = f.readline().split()
    n,s = int(x[0]),int(x[1])


def translate(num, base):
    numex = ''
    while num > 0:
        numex = alphabet[num % base] + numex
        num //= base
    return numex


def pal(num):
    l = len(num) // 2
    for i in range(l):
        if num[i] != num[-1 - i]:
            return False
    return True

k = 0
with open('dualpal.out', 'w+') as f:
    for i in range(s+1,2500000):
        c = 0
        for j in range(2,11):
            if pal(translate(i,j)):
                c += 1
        if c >= 2:
            print(i,file=f)
            k += 1
        if k >= n:
            exit()
