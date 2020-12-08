"""
ID:ayush02
LANG:PYTHON3
TASK:diamond
"""

#C:/Users/ayush/Desktop/USACO/diamond/diamond.in

#reading data from file, storing values of n and k - and putting every diamond size in "input"

with open('C:/Users/ayush/Desktop/USACO/diamond/diamond.in','r') as fin:
    n,k = fin.readline().split()
    n = int(n)
    input = []

    for size in fin.readlines():
        input.append(int(size.strip()))

lst = []
for optimal in input:
    count = 0
    max1 = optimal + int(k)

    for diamond in input:
        if (diamond >= optimal and max1 >= diamond):
            count+=1
            print(optimal,diamond)
    lst.append(count) #just adds count to the list so i can find the maximum later

print(lst)

"""
with open('diamond.in','r') as fin:
    n,k = fin.readline().split()
    n = int(n)
    input = []

    for size in fin.readlines():
        input.append(int(size.strip()))

lst = []
for optimal in input:
    count = 0
    max1 = optimal + int(k)
    for diamond in input:
        if (diamond >= optimal and max1 >= diamond):
            count+=1


    lst.append(count) #just adds count to the list so i can find the maximum later

with open('diamond.out','w') as fout:
    fout.write(str(max(lst)))
"""
