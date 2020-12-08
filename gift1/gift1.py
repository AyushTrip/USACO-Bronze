"""
ID:ayush02
LANG:PYTHON3
TASK:gift1
"""
#Create dictionary
dict = {}
#Read file and set up dictionary
#C:/Users/ayush/Desktop/USACO/gift/gift1.in
fin = open('gift1.in','r')
np = fin.readline()

for i in range(int(np)):
    name = fin.readline().strip()
    dict.update({name:0})

try:
    while True:
        #Start reading giver,reciever,etc.
        giver = fin.readline().strip()
        amount, distribute = fin.readline().split()

        #Convert to integers
        amount = int(amount)
        distribute = int(distribute)

        #calculate amounts
        if distribute == 0 and amount == 0:
            gift =  0
            amount = 0
            leftover = 0
        else:
            gift = amount // distribute
            leftover = amount - (distribute * gift)

        #get recievers
        recievers = []
        for i in range(1,distribute + 1):
            recievers.append(fin.readline().strip())

        #update dictionary
        #Update reciever
        for reciever in recievers:
            newr = dict.get(reciever)
            dict.update({reciever: newr + gift})
        #Update giver
        newg = dict.get(giver)
        dict.update({giver: (newg - amount) + leftover})
        recievers.clear()

except:
    with open('gift1.out','w') as fout:
        for item in dict.items():
            person, balance = item
            balance = str(balance)
            fout.write(person +  " " + balance + '\n')
