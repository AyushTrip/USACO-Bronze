"""
ID:ayush02
LANG:PYTHON3
TASK:blist
"""
def sort_tuple(tup):
    tup.sort(key = lambda x: x[0])
    return tup

info = []
    
#C:/Users/ayush/Desktop/USACO/blist/blist.in
with open('blist.in','r') as fin:
    n = int(fin.readline())
    for line in fin.readlines():
        x, y, z = line.split()
        info.append([int(x), int(y), int(z)])

#Sort the tuples based on start time
sort_tuple(info)
print(info)

#Initilaize arrays
buckets_needed = []

#Find iteration range
first = info[0]
first_iteration = first[0]
last = info[-1]
last_iteration = last[1]


for i in range(first_iteration, last_iteration + 1):
    buckets_at_this_time = 0
    for j in info:
        if j[0] <= i <= j[1]:
            buckets_at_this_time += j[2]
    buckets_needed.append(buckets_at_this_time)

answer= max(buckets_needed)

with open('blist.out', 'w') as fout:
    fout.write(str(answer) + '\n')
