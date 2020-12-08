"""
ID:ayush02
LANG:PYTHON3
TASK:lifeguards
"""
#Function that determines the number of hours covered
#Find all combinations of shift times
#Find maximum of hours worked list

import itertools

#C:/Users/ayush/OneDrive/Desktop/USACO/lifeguards/lifeguards.in
with open('lifeguards.in', 'r') as fin:
    n = fin.readline()
    shift = []
    for line in fin.readlines():
        x, y = line.split()
        shift.append([int(x), int(y)])

#Find all combinations
combinations = []
for item in itertools.combinations(shift, int(n)-1):
    combinations.append(item)

#Find number of hours
#first hour and last hour basically gives me a range of the earliest to latest time
def findrange(combo):
    first = []
    last = []
    for shift in combo:
        first.append(shift[0])
        last.append(shift[1])

    last_hour = max(last)
    first_hour = min(first)

    return first_hour, last_hour

#Setting up final list
answer = []

#Iterate through each combination with one fired lifeguard
for combo in combinations:
    hours = 0
    first, last = findrange(combo)
    #Iterate from every time in between range
    for hour in range(first, last+1):
        for shift in combo:
            #If it falls in range, add one hour
            if shift[0] <= hour < shift[1]:
                hours += 1
                break #IMPORTANT: prevents overcounting

    #Add the hour count for each combination
    answer.append(hours)

#Maximum hours accumulated from the list
final = max(answer)

#Output information
with open('lifeguards.out', 'w') as fout:
    fout.write(str(final))
