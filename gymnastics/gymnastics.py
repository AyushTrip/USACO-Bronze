"""
ID:ayush02
LANG:PYTHON3
TASK:gymnastics
"""
import itertools
def find_pairs(combo, search):
     x, y = combo
     first_line = search[0]

     first_line_x = first_line.index(str(x))
     first_line_y = first_line.index(str(y))
     if min(first_line_x, first_line_y) == first_line_x:
         first = x
         second = y
     else:
        first = y
        second = x

     consistent = True
     for line in search[1::]:
         if line.index(str(second)) < line.index(str(first)):
             return False
     return True


#C:/Users/ayush/Desktop/USACO/gymnastics/gymnastics.in

with open('gymnastics.in','r') as fin:
    #Find k and n values
    k, n = fin.readline().split()
    k = int(k)
    n = int(n)

    #initialize variables
    pairs = 0

    #Read input
    input = []
    for line in fin.readlines():
        input.append(line.strip().split())

#Compute...
lst = []
for i in range(1,n+1):
    lst.append(i)

combinations = itertools.combinations(lst, 2)

pairs = 0

for combo in combinations:
    if find_pairs(combo, input) == True:
        pairs += 1

with open('gymnastics.out','w') as fout:
    fout.write(str(pairs))
