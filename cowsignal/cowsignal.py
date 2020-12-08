"""
ID:ayush02
LANG:PYTHON
TASK:cowsignal
"""
def breakdown(str, k):
    new_string = ''
    for i in str:
        new_string += i*k
    return new_string

#C:/Users/ayush/OneDrive/Desktop/USACO/cowsignal/cowsignal.in
with open('cowsignal.in', 'r') as fin:
    m, n, k = map(int, fin.readline().split())
    signals = []
    for i in range(m):
        signals.append(fin.readline().strip())

with open('cowsignal.out', 'w') as fout:
    for signal in signals:
        for i in range(k):
            fout.write(breakdown(signal, k) + '\n')
