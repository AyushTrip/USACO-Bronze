"""
ID:ayush02
LANG:PYTHON3
TASK:hps
"""
#C:/Users/ayush/Desktop/USACO/hps/hps.in
with open('hps.in', 'r') as fin:
    games = []
    n = fin.readline()
    for game in fin.readlines():
        num1, num2 = game.strip().split()
        num1 = int(num1)
        num2 = int(num2)
        games.append([num1,num2])

case1 = ([1,2],[2,3],[3,1])
case2 = ([1,3],[3,2],[2,1])
case3 = ([2,1],[1,3],[3,2])
case4 = ([2,3],[3,1],[1,2])
case5 = ([3,1],[1,2],[2,3])
case6 = ([3,2],[2,1],[1,3])

sum1 = 0
sum2 = 0
sum3 = 0
sum4 = 0
sum5 = 0
sum6 = 0
ties = 0

for game in games:
    first, second = game
    if first == second:
        ties += 1
    elif game in case1:
        sum1 += 1
    elif game in case2:
        sum2 += 1
    elif game in case3:
        sum3 += 1
    elif game in case4:
        sum4 += 1
    elif game in case5:
        sum5 += 1
    elif game in case6:
        sum6 += 1

final = []
final.append(sum1)
final.append(sum2)
final.append(sum3)
final.append(sum4)
final.append(sum5)
final.append(sum6)



answer = max(final)

with open('hps.out', 'w') as fout:
    fout.write(str(answer)+'\n')
