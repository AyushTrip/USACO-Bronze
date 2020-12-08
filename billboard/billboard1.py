"""
ID=ayush02
LANG:PYTHON3
TASK:billboard
"""
#1 1 5 5
# 6 6 9 9
#38 38 60 60

#IF RUNNING PROGRAM CHANGE NAME


#define is overlap - use later in program
def IsOverlap(r1x1,r1y1,r1x2,r1y2,r2x1,r2y1,r2x2,r2y2):
    if (r1x2 <  r2x1) or (r2x2 < r1x1):
        return False

    if (r1y2 < r2y1) or (r2y2 < r1y1):
        return False
    return True

#Find area of overlap
def Overlap_Area(r1x1,r1y1,r1x2,r1y2,r2x1,r2y1,r2x2,r2y2):
    bottomx = max(r1x1,r2x1)
    bottomy = max(r1y1,r2y1)

    topx = min(r1x2,r2x2)
    topy = min(r1y2, r2y2)

    diffx = abs(topx - bottomx)
    diffy = abs(topy - bottomy)

    overlap = diffx * diffy
    return overlap

def Regular_Area(a,b,c,d):
    diffx = abs(a - c)
    diffy = abs(b - d)
    area = diffx * diffy
    return area

#open file, read input
#C:/Users/ayush/Desktop/USACO/billboard/billboard.in
input_array = []
with open('billboard.in') as fin:
    matrix = fin.readlines()
    for line in matrix:
        input_array.append(line.strip())

#Take coordinates
billboard1, billboard2,truck = input_array
r1x1,r1y1,r1x2,r1y2 = billboard1.split()
r2x1,r2y1,r2x2,r2y2 = billboard2.split()
t1x1,t1y1,t1x2,t1y2 = truck.split()
#Convert all to integers
r1x1 = int(r1x1)
r1x2 = int(r1x2)
r1y1 = int(r1y1)
r1y2 = int(r1y2)
r2x1 = int(r2x1)
r2x2 = int(r2x2)
r2y1 = int(r2y1)
r2y2 = int(r2y2)
t1x1 = int(t1x1)
t1y1 = int(t1y1)
t1x2 = int(t1x2)
t1y2 = int(t1y2)


#Apply functions and code

if IsOverlap(r1x1,r1y1,r1x2,r1y2,t1x1,t1y1,t1x2,t1y2) == False and IsOverlap(r2x1,r2y1,r2x2,r2y2,t1x1,t1y1,t1x2,t1y2) == False:
    area1 = Regular_Area(r1x1,r1y1,r1x2,r1y2)
    area2 = Regular_Area(r2x1,r2y1,r2x2,r2y2)
    total_area = area1 + area2
if IsOverlap(r1x1,r1y1,r1x2,r1y2,t1x1,t1y1,t1x2,t1y2) == True and IsOverlap(r2x1,r2y1,r2x2,r2y2,t1x1,t1y1,t1x2,t1y2) == False:
    area1 = Regular_Area(r1x1,r1y1,r1x2,r1y2) - Overlap_Area(r1x1,r1y1,r1x2,r1y2,t1x1,t1y1,t1x2,t1y2)
    area2 = Regular_Area(r2x1,r2y1,r2x2,r2y2)
    total_area = area1+ area2
if IsOverlap(r1x1,r1y1,r1x2,r1y2,t1x1,t1y1,t1x2,t1y2) == True and IsOverlap(r2x1,r2y1,r2x2,r2y2,t1x1,t1y1,t1x2,t1y2) == True:
    area1 = Regular_Area(r1x1,r1y1,r1x2,r1y2) - Overlap_Area(r1x1,r1y1,r1x2,r1y2,t1x1,t1y1,t1x2,t1y2)
    area2 = Regular_Area(r2x1,r2y1,r2x2,r2y2) - Overlap_Area(r2x1,r2y1,r2x2,r2y2,t1x1,t1y1,t1x2,t1y2)
    total_area = area1 + area2

#WRITE ANSWER TO FILE
with open('billboard.out','w') as fout:
    fout.write(str(total_area) + '\n')
