"""
ID: ayush02
LANG: PYTHON3
TASK: oddphoto
"""

#Read input and cow list
n = int(input())
raw_cows = list(map(int, input().split()))

#This is to convert all the stuff to even and odd values: 'O' and 'E' values
even, odd = 0, 0
for i in raw_cows:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

#Initialize some idot stuff
iteration = 0
groups = 0

#Main loop
while True:
    #Even group - if the iteration is even and the group requires even number
    if even > 0:
        even -= 1
        groups += 1
    elif odd >= 2:
        odd -= 2
        groups += 1

    #Either remove one even or two odds
    else:
        break

    #Odd group - if the iteration if odd and the group requires odd number
    if odd >= 1:
        odd -= 1
        groups += 1

    #Remove one odd number if possible
    else:
        break

## NOTE: Break out of the loop IF ANY CONDITION fails
## because that means that no more groups can be created

#Deal with leftover values after the main iteration
if odd > 0 and groups > 1:
    answer = groups - 1
else:
    answer = groups

#Print idot answer
print(answer)
