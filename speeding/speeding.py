"""
ID: ayush02
LANG: PYTHON3
TASK: speeding
"""

#C:/Users/ayush/OneDrive/Desktop/USACO/bronze/M-Z/speeding/speeding.in
with open('speeding.in', 'r') as fin:
    n, m = map(int, fin.readline().split())

    limits = []

    for i in range(n):
        segment, limit = map(int, fin.readline().split())
        for j in range(segment):
            limits.append(limit)

    bessie = []
    for i in range(m):
        bessie_segment, bessie_limit = map(int, fin.readline().split())
        for j in range(bessie_segment):
            bessie.append(bessie_limit)

    compare = list(zip(limits, bessie))

    answer = 0

    for i in compare:
        sl, bs = i
        if bs - sl > answer:
            answer = (bs - sl)

with open('speeding.out', 'w') as fout:
    fout.write(str(answer) + '\n')
