"""
ID:ayush02
LANG:PYTHON3
TASK:teleport
"""
#C:/Users/ayush/Desktop/USACO/teleport/teleport.in
with open('teleport.in', 'r') as fin:
    a, b, x, y = fin.readline().split()
    a = int(a)
    b = int(b)
    x = int(x)
    y = int(y)

#Find absolute teleportation without any magic trix
absolute_distance = abs(a-b)

first_teleport = abs(x - a)
second_teleport = abs(y - a)

if min(first_teleport, second_teleport) == first_teleport:
    closest = x
    farthest = y

else:
    closest = y
    farthest = x

possible_answer = []

#Check if closer teleporter is in between
possible_answer.append(absolute_distance)
possible_answer.append(abs(closest - a) + abs(farthest - b))


answer = min(possible_answer)
with open('teleport.out', 'w') as fout:
    fout.write(str(answer) + '\n')
