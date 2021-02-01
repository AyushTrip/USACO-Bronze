"""
ID: ayush02
LANG: PYTHON3
TASK: word
"""

#C:/Users/ayush/OneDrive/Desktop/USACO/M-Z/word/word.in
with open('C:/Users/ayush/OneDrive/Desktop/USACO/M-Z/word/word.in', 'r') as fin:
    n, k = map(int, fin.readline().split())
    words = list(fin.readline().split())


#C:/Users/ayush/OneDrive/Desktop/USACO/M-Z/word/word.out
with open('C:/Users/ayush/OneDrive/Desktop/USACO/M-Z/word/word.out', 'w') as fout:
    current_length = 0
    current_line = []

    for i in range(len(words)):
        word = words[i]
        if len(word) + current_length <= k:
            current_length += len(word)
            fout.write(' ' + word)
        else:
            current_length = len(word)
            fout.write('\n' + word)
