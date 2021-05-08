"""
ID: kqanto1
LANG: PYTHON3
TASK: friday
"""
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = 1
friday_days = [0] * 7

with open('friday.in', 'r') as f:
    n = int(f.readline())

for k in range(1900, 1900 + n):
    if (k % 4 == 0 and k % 100 != 0 or k % 400 == 0) and k != 0:
        month[1] += 1
    for i in range(len(month)):
        for day in range(1, month[i] + 1):
            if day == 13:
                days += 12
                friday_days[days % 7] += 1
        days += month[i] - 12
    if (k % 4 == 0 and k % 100 != 0 or k % 400 == 0) and k != 0:
        month[1] -= 1

with open('friday.out', 'w+') as f:
    print(friday_days[6], end=' ', file=f)
    for i in range(5):
        print(friday_days[i], end=' ', file=f)
    print(friday_days[5], end='', file=f)
    print(file=f)
