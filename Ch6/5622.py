import sys

dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
T = sys.stdin.readline()

time = 0

for i in range(len(T)):
    for j in dial:
        if T[i] in j:
            time += dial.index(j) + 3

print(time)