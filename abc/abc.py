import itertools
inp = list(str(input()).split())

numbers = []
for i in inp:
    numbers.append(int(i))
numbers.sort()


pa = []
for i in range(6):
    pa.append(numbers[i])

combs = itertools.combinations(pa, 3)

def valid(combination):
    valid = True
    stuff = []
    global numbers
    a, b, c = combination
    ab = a + b
    bc = b + c
    ac = a + c
    abc = a + b + c
    stuff.append(ab)
    stuff.append(bc)
    stuff.append(ac)
    stuff.append(abc)

    for value in stuff:
        if value not in numbers:
            valid = False
            break

    return valid

for i in combs:
    if valid(i) == True:
        answer = i

a,b,c = answer
print(str(a) + ' ' + str(b) + ' ' + str(c))
