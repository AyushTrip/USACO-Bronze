"""
ID:ayush02
LANG:PYTHON3
TASK:whereamii
"""
#Import modules
import itertools
import re

#C:/Users/ayush/OneDrive/Desktop/USACO/whereami/whereami.in
with open('C:/Users/ayush/OneDrive/Desktop/USACO/whereami/whereami.in', 'r') as fin:
    n = int(fin.readline())
    sequence = ''
    sequence += fin.readline().strip()

#Given a list, determine if it is valid based on if it is all one's
def is_valid(occurance_list):
    valid = True
    setone = set(occurance_list)
    for i in setone:
        if i > 1:
            valid = False
            break
    return valid

#Extra Test Cases
main = []
for k in range(n):
    occurances = []
    for i in range(0,n-k):
        occurances.append(sequence.count(sequence[i:i+k]))
    main.append(occurances)

answer = 0
for sublist in main:
    if is_valid(sublist) == True:
        break
    else:
        answer += 1
'''
with open('whereami.out', 'w') as fout:
    fout.write(str(answer) + '\n')
'''

print(answer)



















'''
ATTEMPT ONE
#Characters list for the reduced permutation time
#Total sequence list


#ALL substring occurances in a string
def find_unique(substring, sequence):
    matches = [i.start() for i in re.finditer(substring, sequence)]
    return len(matches)


#For each value in range of the characters length

occurances = []
for i in range(1, len(characters)+1):
    #Initialize the amount of occurances of each combination in the sequence
    mailbox_permutations = itertools.permutations(characters, i)
    #print(i, [i for i in mailbox_permutations])
    occurances.append([find_unique(''.join(k), sequence) for k in mailbox_permutations])

dumplist = []
for sublist in occurances:
    for i in sublist:
        if i > 1:
            dumplist.append(sublist)

answer = 0
for sublist in dumplist:
    if sublist in occurances:
        answer += 1
        occurances.remove(sublist)

print(answer)
'''
