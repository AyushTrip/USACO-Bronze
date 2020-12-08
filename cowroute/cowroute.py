"""
ID:ayush02
LANG:PYTHON3
TASK:cowroute
"""

#Open file and read information
#C:/Users/ayush/Desktop/USACO/cowroute/cowroute.in
with open('cowroute.in','r') as fin:
    a,b,n = fin.readline().split()
    n = int(n)
    final_cost = [] #Find min of list at end
    for i in range(1,n+1):
        cost,cities = fin.readline().split()
        route = fin.readline()
        if a in route:
            if b in route:
                try:
                    if route.split().index(a) < route.split().index(b):
                        final_cost.append(int(cost))
                except ValueError:
                    pass

if final_cost == []:
    answer = "-1"
else:
    answer = min(final_cost)


with open('cowroute.out','w') as fout:
    fout.write(str(answer))
