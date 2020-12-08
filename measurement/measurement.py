"""
ID:ayush02
LANG:PYTHON
TASK:measurement
"""

#C:/Users/ayush/OneDrive/Desktop/USACO/measurement/measurement.py
with open('measurement.in', 'r') as fin:
    n = int(fin.readline())
    logs = []
    for i in range(n):
        log = fin.readline().strip()
        day, name, change = log.split()
        logs.append([day, name, change])
    logs.sort(key=lambda x: int(x[0]))

    #[['1', 'Bessie', '+2'], ['4', 'Elsie', '-1'], ['7', 'Mildred', '+3'], ['9', 'Mildred', '-1']]

milking = {}
for log in logs:
    milking.update({log[1]:7})

#Scan through each log
winners = []
temp = []

for log in logs:
    num, name, change = log
    operation, number = change

    temp.clear()

    cow_milk = str(milking.get(name))
    expression = cow_milk + operation + number
    new_value = eval(expression)
    milking.update({name:new_value})

    record = max(milking.values())
    for log in milking.keys():
        if milking.get(log) == record:
            temp.append(log)

    winners.append([i for i in temp])

#[['Bessie'], ['Bessie'], ['Mildred'], ['Bessie', 'Mildred']]


def new_display(hof):
    new = 1
    fame_length = len(hof)
    for display in range(1,fame_length):
        if hof[display] != hof[display-1]:
            new += 1
    return new

answer = new_display(winners)
with open('measurement.out', 'w') as fout:
    fout.write(str(answer) + '\n')
