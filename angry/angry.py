"""
ID:ayush02
LANG:PYTHON3
TASK:angry
"""

#C:/Users/ayush/OneDrive/Desktop/USACO/angry/angry.in

with open('angry.in', 'r') as fin:
    n = int(fin.readline())
    nums = []
    for i in fin.readlines():
        nums.append(int(i.strip()))
    nums.sort()

print('Sequence: '+ str(nums) + '\n')

def all_unsatisfy(lst):
    global nums
    bad = True
    for i in lst:
        if i in nums:
            bad = False
            return bad
    return bad

def sequence_positive(num):
    global nums
    blast_radius = 1
    current_bomb = num

    blast_sequence = [num]
    answer = []

    valid = True
    while valid == True:
        next_blast = current_bomb + blast_radius
        temp_range = list([i for i in range(next_blast, current_bomb, -1)])
        for i in temp_range:
            if i in nums:
                for j in range(current_bomb+1, i+1):
                    blast_sequence.append(j)
                current_bomb = i
                blast_radius += 1
                break

            if all_unsatisfy(temp_range) == True:
                valid = False

    for i in blast_sequence:
        if i in nums:
            answer.append(i)

    return answer


def sequence_negative(num):
    global nums
    blast_radius = 1
    current_bomb = num

    blast_sequence = [num]
    answer = []

    valid = True
    while valid == True:
        next_blast = current_bomb - blast_radius
        temp_range = list([i for i in range(next_blast, current_bomb)])
        for i in temp_range:
            if i in nums:
                for j in range(next_blast, current_bomb):
                    blast_sequence.append(j)
                current_bomb = i
                blast_radius += 1
                break

            if all_unsatisfy(temp_range) == True:
                valid = False

    for i in blast_sequence:
        if i in nums:
            answer.append(i)

    return answer


sequence = []
for num in nums:
    answer = set(sequence_positive(num) + sequence_negative(num))
    sequence.append([num, answer])

sequence.sort(key=lambda x:len(x[1]))
final = len(sequence[-1][1])

with open('angry.out', 'w') as fout:
    fout.write(str(final) + '\n')
