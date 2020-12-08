"""
ID:ayush02
LANG:PYTHON3
TASK:lineup
"""
import itertools
from operator import itemgetter

#C:/Users/ayush/OneDrive/Desktop/USACO/lineup/lineup.in
with open('lineup.in', 'r') as fin:
    n = int(fin.readline())
    pairings_list = []
    appearances = []
    for i in range(n):
        pairing = fin.readline().split()
        pairings_list.append([pairing[0], pairing[5]])

def is_valid(lst):
    global pairings_list
    good = True
    for pairing in pairings_list:
        x,y = pairing
        if abs(lst.index(x) - lst.index(y)) != 1:
            good = False
    return good




#Set lists for the next step
cows = ['Bessie', 'Buttercup', 'Belinda', 'Beatrice', 'Bella', 'Blue', 'Betsy','Sue']
cow_permutations_raw = list(itertools.permutations(cows, 8))
cow_permutations_raw.sort(key=lambda x:"".join([k.lower() for k in x]))

valid_sublists = []
valid_sublists.append([lst for lst in cow_permutations_raw if is_valid(lst) == True])

anstuple = valid_sublists[0][0]
answer = []
answer.append([i for i in anstuple])

with open('lineup.out', 'w') as fout:
    for i in answer[0]:
        fout.write(str(i) + '\n')
