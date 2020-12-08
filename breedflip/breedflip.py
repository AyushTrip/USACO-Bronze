"""
ID:ayush02
LANG:PYTHON3
TASK:breedflip
"""

#C:/Users/ayush/OneDrive/Desktop/USACO/breedflip/breedflip.in

with open('breedflip.in', 'r') as fin:
    n = int(fin.readline())
    seqa = fin.readline()
    seqb = fin.readline()

#Locate all the wrongly positioned or wrong identity cows
confliction = []
for i in range(n):
    if seqa[i] != seqb[i]:
        confliction.append(i)

answer = 0
for i in confliction:
    if (i+1) not in confliction:
        answer += 1

with open('breedflip.out', 'w') as fout:
    fout.write(str(answer))
