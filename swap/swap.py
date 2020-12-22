"""
ID:ayush02
LANG:PYTHON3
TASK:swap
"""

#C:/Users/dhruvpra/OneDrive - Intel Corporation/Desktop/USACO/swap/swap.in
with open('swap.in', 'r') as fin:
    n, k = map(int, fin.readline().split())
    a1, a2 = map(int, fin.readline().split())
    b1, b2 = map(int, fin.readline().split())

def simulate(order, a1, a2, b1, b2):
    beginning = []
    middle = []
    end = []

    a1 -= 1
    a2 -= 1
    b1 -= 1
    b2 -= 1

    #Determine A swaps
    for i in order[0:a1]:
        beginning.append(i)
    for j in order[a2:a1-1:-1]:
        middle.append(j)
    for k in order[a2+1:]:
        end.append(k)

    order = beginning + middle + end

    #Determine B swaps
    beginning = []
    middle = []
    end = []

    for i in order[0:b1]:
        beginning.append(i)
    for j in order[b2:b1-1:-1]:
        middle.append(j)
    for k in order[b2+1:]:
        end.append(k)

    order = beginning + middle + end
    return order

#Set up variables and cow order
original = []
cows = []
for i in range(1,n+1):
    original.append(str(i))
    cows.append(str(i))

#Locate the cycle frequency
iterations = 0
while True:
    cows = simulate(cows, a1, a2, b1, b2)
    if cows == original:
        break
    else:
        iterations += 1

#Determine number of swaps
swaps = k % iterations

#Calculate the new orders
for i in range(swaps):
    cows = simulate(cows, a1, a2, b1, b2)


with open('swap.out', 'w') as fout:
    for i in cows:
        fout.write(i + '\n')



"""
for i in range(k):
    cows = simulate(cows, a1, a2)
    cows = simulate(cows, b1, b2)

print([i + '\n' for i in cows])

with open('swap.out', 'w') as fout:
    for i in cows:
        fout.write(i + '\n')
"""
