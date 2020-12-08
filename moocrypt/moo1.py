"""
ID:ayush02
LANG:PYTHON3
TASK:moocrypt
"""
import itertools
#Check horizontal strings
def check_horizontal(combination):
    search_string = []
    global matrix
    m, o = combination
    count = 0
    search_string.append(m + o + o)
    search_string.append(o + o + m)
    for line in matrix:
        for type in search_string:
            if type in line:
                count += 1
    return count

#Check vertical strings
def check_vertical(combination, length):
    search_string = []
    global matrix

    m, o = combination
    count = 0

    f = m + o + o
    forward = "".join(f)
    b = o + o + m
    backward = "".join(b)

    for i in range(length):
        vert = []
        for line in matrix:
            vert.append(line[i])

        vert2 = "".join(vert)
        if forward in vert2 or backward in vert2:
            count += 1

    return count

#Check diagonal strings
def check_diagonal(first, second, length, width):

    count = 0

    #Globalized values
    global matrix

    for n in range(length):
        for m in range(width):
            if matrix[n][m]== first:
                #Move in all four directions
                #Top right
                if n >= 2 and m <= (width - 2):
                    try:
                        if matrix[n-1][m+1] == second and matrix[n-2][m+2] == second:
                            count += 1
                    except:
                        pass
                #Bottom Left
                if n <= (length - 2) and m >= 2:
                    try:
                        if matrix[n+1][m-1] == second and matrix[n+2][m-2] == second:
                            count += 1
                    except:
                        pass
                #Bottom right
                if n <= (length - 2) and m <= (width - 2):
                    try:
                        if matrix[n+1][m+1] == second and matrix[n+2][m+2] == second:
                            count += 1
                    except:
                        pass
                #Top Left
                if n >= 2 and m >= 2:
                    try:
                        if matrix[n-1][m-1] == second and matrix[n-2][m-2] == second:
                            count += 1
                    except:
                        pass
    return count


#Begin reading input
#Full Path # NOTE: 'C:/Users/ayush/OneDrive/Desktop/USACO/moocrypt/moocrypt.in'
with open('moocrypt.in', 'r') as fin:
    n, m = map(int, fin.readline().split())
    matrix = []
    for line in fin.readlines():
        matrix.append(line.strip())

#Find all combinations
alphabet = []
for line in matrix:
    for letter in line:
        if letter not in alphabet:
            alphabet.append(letter)

#Use itertools to compute combinations
combinations = list(itertools.permutations(alphabet, 2))

answers = []
for combo in combinations:
    x = check_horizontal(combo)
    y = check_vertical(combo, m)
    first, second = combo
    z = check_diagonal(first, second, n, m)
    answers.append(x+y+z)

final = max(answers)

with open('moocrypt.out','w') as fout:
    fout.write(str(final)+'\n')
