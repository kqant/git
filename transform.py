"""
ID: kqanto1
LANG: PYTHON3
TASK: transform
"""
import copy


def turn(m):
    return[list(reversed(col)) for col in zip(*m)]


def reflection(matr):
    m = copy.deepcopy(matr)
    for i in range(n):
        for j in range(n // 2):
            m[i][j], m[i][-1 - j] = m[i][-1 - j], m[i][j]
    return m


kon = []
orig = []
with open("transform.in", 'r') as f:
    n = int(f.readline())
    for i in range(n):
        s = f.readline().split()[0]
        orig.append(list(s))
    for i in range(n):
        s = f.readline().split()[0]
        kon.append(list(s))
f = open('transform.out','w+')
if kon == turn(orig):
    f.write(f'1\n')
elif kon == turn(turn(orig)):
    f.write(f'2\n')
elif kon == turn(turn(turn(orig))):
    f.write(f'3\n')
elif kon == reflection(orig):
    f.write(f'4\n')
elif kon == turn(reflection(orig)) or kon == turn(turn(reflection(orig))) or kon == turn(turn(turn(reflection(orig)))):
    f.write(f'5\n')
elif orig == kon:
    f.write(f'6\n')
else:
    f.write(f'7\n')