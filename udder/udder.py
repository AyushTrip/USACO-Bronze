"""
ID: ayush02
LANG: PYTHON3
TASK: udder
"""
cowphabet = str(input())
phrase = str(input())
answer = 1
for i in range(0, len(phrase)-1):
    current_position = cowphabet.index(phrase[i])
    next_position = cowphabet.index(phrase[i+1])

    if next_position <= current_position:
        answer += 1
print(answer)
