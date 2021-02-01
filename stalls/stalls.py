"""
ID: ayush02
LANG: PYTHON3
TASK: stalls
"""

n = int(input())
cows = list(map(int, input().split()))
stalls = list(map(int, input().split()))

cows.sort(reverse=True)
stalls.sort(reverse=True)

permutations = []

for i in cows:
    perm = 0
    temp = []

    for j in stalls:
        if j >= i:
            perm += 1
            if perm == 1:
                temp.append(j)

    stalls.remove(temp[0])
    permutations.append(perm)


answer = 1
for i in permutations:
    answer *= i

print(answer)
