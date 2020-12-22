import itertools
import statistics

def represents_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

n = int(input())
seqraw = list(str(input()).split())

sequence = []
for i in seqraw:
    sequence.append(str(i))

#Compute every single IJ photo
#and detemrmine the average flower of each
numbers = list([i for i in range(1,n+1)])

combs = itertools.combinations(numbers, 2)
combinations = []
combinations.append([i for i in combs])


subsets = []
answer = 0

subsets = []
averages = []

for combination in combinations[0]:
    petals = []
    i, j = combination
    for i in range(i-1, j):
        petals.append(int(sequence[i]))

    subsets.append(petals)

    avg = statistics.mean(petals)
    average = '%g'%(avg)

    if represents_int(average) == True:
        if average in sequence:
            averages.append(average)


for i in subsets:
    for j in averages:
        if int(j) in i:
            answer += 1
            break

print(answer)
