"""
ID:ayush02
LANG:PYTHON3
TASK:marathon
"""
def distance(x1,y1,x2,y2):
    return (abs(x2-x1) + abs(y2-y1))

with open('marathon.in', 'r') as fin:
    n = int(fin.readline())
    coordinates = fin.readlines()

save = []
total = 0

for i in range(n-1):

    if i < n-2:
        current = coordinates[i].strip()
        skip = coordinates[i+1].strip()
        nextc = coordinates[i+2].strip()

        #annoying conversions
        x1, y1 = current.split()
        x1 = int(x1)
        y1 = int(y1)

        x2, y2 = skip.split()
        x2 = int(x2)
        y2 = int(y2)

        x3, y3 = nextc.split()
        x3 = int(x3)
        y3 = int(y3)

        #calculations
        total += distance(x1,y1,x2,y2)
        original_distance = distance(x1,y1,x2,y2) + distance(x2,y2,x3,y3)
        new_distance = distance(x1,y1,x3,y3)
        distance_saved = original_distance - new_distance

        save.append(distance_saved)

    else:
        x1, y1 = coordinates[-2].split()
        x1 = int(x1)
        y1 = int(y1)
        x2,y2 = coordinates[-1].split()
        x2 = int(x2)
        y2 = int(y2)

        total +=
        total += distance(x1,y1,x2,y2)

answer = total - max(save)

with open('marathon.out','w') as fout:
    fout.write(str(answer)+'\n')
