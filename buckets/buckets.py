"""
ID:ayush02
LANG:PYTHON3
TASK:buckets
"""

#C:/Users/ayush/OneDrive/Desktop/USACO/buckets/buckets.in
with open('buckets.in', 'r') as fin:
    maze = []
    for line in fin.readlines():
        maze.append(line.strip())

lake = []
rock = []
barn = []

#Find coordinates of each locations
for y in range(10):
    for x in range(10):
        if maze[y][x] == 'L':
            lake = [x,y]
        if maze[y][x] == 'R':
            rock = [x,y]
        if maze[y][x] == 'B':
            barn = [x,y]

#Case One - Rock Intersection --
blocked = False
rock_x = rock[0]
rock_y = rock[1]

barn_x = barn[0]
barn_y = barn[1]

lake_x = lake[0]
lake_y = lake[1]

if rock_x == barn_x and rock_x == lake_x:
    if lake_y < rock_y < barn_y or barn_y < rock_y < lake_y:
        blocked = True

if rock_y == barn_y and rock_y == lake_y:
    if lake_x < rock_x < barn_x or barn_x < rock_x < lake_x:
        blocked = True

#Final calculation
net_x = abs(barn_x - lake_x)
net_y = abs(barn_y - lake_y)
net_distance = net_x + net_y - 1

if blocked == True:
    answer = net_distance + 2
else:
    answer = net_distance

with open('buckets.out','w') as fout:
    fout.write(str(answer) + '\n')
