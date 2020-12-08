"""
ID:ayush02
LANG:PYTHON
TASK:cbarn
"""

#C:/Users/ayush/OneDrive/Desktop/USACO/cbarn/cbarn.in
with open('cbarn.in', 'r') as fin:
    n = int(fin.readline())
    sequence = []
    for i in range(n):
        sequence.append(str(fin.readline().strip()))

orders = []

#Sort each possible permutation order
indice = 0
for i in sequence:
    modified = []

    if indice == 0:
        for i in sequence[indice::]:
            modified.append(i)

    if indice > 0:
        for i in sequence[indice::]:
            modified.append(i)
        for j in sequence[0:indice:]:
            modified.append(j)

    orders.append([modified, indice])
    indice += 1

def calculate_distance(lst):
    length = len(lst)
    answer = 0
    for i in range(length):
        answer += i * int(lst[i])
    return answer


#Calculate the distance of each combination and append it to distances
distances = []
for order in orders:
    lst, indice = order
    distances.append([calculate_distance(lst), indice])

distances.sort(key = lambda x: x[0])

answer = distances[0][0]
with open('cbarn.out', 'w') as fout:
    fout.write(str(answer) + '\n')
