"""
ID: kqanto1
LANG: PYTHON3
TASK: palsquare
"""
alphabet = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
with open('palsquare.in', 'r') as f:
    n = int(f.readline())


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


with open('palsquare.out', 'w') as f:
    for i in range(1, 301):
        if pal(translate(i * i, n)):
            print(translate(i, n), translate(i * i, n), file=f)
