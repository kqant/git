from itertools import *
"""
ID: kqanto1
LANG: PYTHON3
TASK: crypt1
"""

def foo(n):
    n = list(str(n))
    n = list(map(int,n))
    for x in n:
        if not(x in d):
            return False
    return True

dig1 = []
dig2 = []
with open('crypt1.in','r') as f:
    n = f.readline().split()
    n = int(n[0])
    d = list(map(int,f.readline().split()))

c = 0
p1 = product(d,d,d)
p2 = product(d,d)
otv = []
for x in p1:
    dig1.append(''.join(map(str,x)))
for x in p2:
    dig2.append(''.join(map(str,x)))
dig1 = list(map(int,dig1))
dig2 = list(map(int,dig2))
for x in dig1:
    for y in dig2:
        if len(str(x*(y%10))) == 3 and len(str(x*(y//10))) == 3 and foo(x*(y%10)) and foo(x*(y//10)):
            if foo(x*y):
                c += 1
                print(x*y)
f = open('crypt1.out','w+')
f.write(f'{c}\n')


