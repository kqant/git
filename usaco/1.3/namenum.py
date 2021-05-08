"""
ID: kqanto1
LANG: PYTHON3
TASK: namenum
"""
d = {'A':2, 'B':2, 'C':2, 'D':3, 'E':3, 'F':3, 'G':4, 'H':4, 'I':4, 'J':5, 'K':5, 'L':5,
            'M':6, 'N':6, 'O':6, 'P':7, 'R':7, 'S':7, 'T':8, 'U':8, 'V':8, 'W':9, 'X':9, 'Y':9}

names = []
namesn = []
with open("namenum.in", 'r') as f:
    n = int(f.readline())
with open('dict.txt', 'r') as f:
    for i in range(4617):
        k = f.readline().split()[0]
        if not('Q' in k or 'Z' in k):
            names.append(k)
for i in range(len(names)):
    tmp = list(names[i])
    for j in range(len(tmp)):
        tmp[j] = d[tmp[j]]
    namesn.append(int(''.join(map(str,tmp))))
find = True
with open("namenum.out", 'w+') as f:
    for i in range(len(names)):
        if n == namesn[i]:
            f.write(f"{names[i]}\n")
            find = False
    if find:
        f.write(f"NONE\n")


