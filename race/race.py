"""
ID:ayush02
LANG:PYTHON3
TASK:race
"""
with open('C:/Users/ayush/OneDrive/Desktop/USACO/race/race.in', 'r') as fin:
    k, n = fin.readline().split()
    x_values = []
    for x in fin.readlines():
        x_values.append(int(x))

def next_number(num, x, distance_traveled, k):
    #parameters = [3, 1, 6, 10]

    options = []
    for i in range(-1,2):
        options.append(num+i)

    #options - [2, 3, 4]
    for value in options:
        new_distance = distance_traveled + value
        distance_left =  k - new_distance
        old_distance = new_distance - distance_traveled

        if new_distance >= k and value == x:
            return value

        if distance_left == old_distance:
            return value





'''
for x in x_values:
    distance_traveled = 0
    speed = 0
    count = 0
    ## NOTE: Add one to final answer to accomodate for final speed value
    while distance_traveled <= int(k):
        speed += 1
        next_numb = next_number(speed, x, distance_traveled, int(k))
        if next_numb[1] == 'True':
            print(count)
            break
        else:
            distance_traveled += speed
            count += 1
'''
