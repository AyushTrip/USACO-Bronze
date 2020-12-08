"""
ID:ayush02
LANG:PYTHON3
TASK:crossroad
"""
#C:/Users/ayush/Desktop/USACO/crossroad/crossroad.in
count = 0
lst = []
#C:/Users/ayush/Desktop/USACO/crossroad/crossroad.in
#Open file and read data
with open('crossroad.in','r') as fin:
    n = fin.readline()
    observations = fin.readlines()
    for line in observations:
        lst.append(line)

lst2 = []


#Iterate through 1-10 to solve
for id in range(1,11):
    location = None #set location to null before each iteration
    for log in lst:
        cow, side = log.split()
        cow = int(cow)
        side = int(side)
        if cow == id: #Check if the ID matches the current iteration
            lst2.append(id)
            if side != location:
                count += 1
                location = side
            else:
                location = side

answer = count - len(set(lst2))

with open('crossroad.out','w') as fout:
    fout.write(str(answer))

#FUTURE REFERECE: In this program, I took a series of steps to determine the number of crossings
#1. Iterate through 1-10 so I can have a makeshift sort through all the types of cows. Also initiazlize the location.
#2. Iterate through each log, if the ID matches the current iteration from 1-10, act on it
#3. Set conditions. If the location matches the log, pass. Otherwise, it means a new crossing happened - so add 1
#4. Find the total for count, and subtract the set of cow ID's. This is because the program thinks the first appearance of a cow is ALWAYS a crossing.
#4 cont. By subtracting the length of the set, we derive the exact amount of crossings that occured
