"""
ID:ayush02
LANG:PYTHON3
TASK:triangles
"""
import itertools

def valid_triangle(vertex, point1, point2):
    x_cord, y_cord = vertex
    if point1[0] == x_cord and point2[1] == y_cord:
        return True

def find_area(vertex, point1, point2):
    base1 = abs(point1[0] - vertex[0])
    height1 = abs(point2[1] - vertex[1])

    base2 = abs(point2[0] - vertex[0])
    height2 = abs(point1[1] - vertex[1])

    return max((base2 * height2 / 2), (base1 * height1 / 2))

#Full path: C:/Users/ayush/OneDrive/Desktop/USACO/triangles/triangles.in
with open('triangles.in', 'r') as fin:
    n = int(fin.readline())
    coordinates = []
    for i in range(n):
        x, y = map(int, fin.readline().split())
        coordinates.append([x, y])

#Find vertex coordinate
combinations = list(itertools.permutations(coordinates, 3))

valid = []
for combo in combinations:
    vertex, point1, point2 = combo
    if valid_triangle(vertex, point1, point2) == True:
        valid.append(combo)

area = []
for combo in valid:
    vertex, point1, point2 = combo
    area.append(find_area(vertex, point1, point2))

answer = max(area)

with open('triangles.out', 'w') as fout:
    fout.write(str(int(answer * 2)))
