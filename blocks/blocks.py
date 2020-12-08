"""
ID:ayush02
LANG:PYTHON3
TASK:blocks
"""
#Import module
#Define funtion

#Set dictionary
alphabet = "abcdefghijklmnopqrstuvwxyz"
maxdict = {}
mydict = {}
for i in alphabet:
    mydict.update({i:0})

#Compute...
#C:/Users/ayush/Desktop/USACO/blocks/blocks.in
with open('blocks.in', 'r') as fin:
    n = int(fin.readline())
    input = fin.readlines()

for line in input:
    word1, word2 = line.split()
    for i in alphabet:
        answer = max(word1.count(i), word2.count(i))
        new = mydict.get(i)
        maxdict.update({i:answer})
        mydict.update({i:answer+new})

    maxdict.clear()

print(mydict.values())

#Output
with open('blocks.out','w') as fout:
    for i in alphabet:
        fout.write(str(mydict.get(i)) + '\n')

#22210110000000200111100100
