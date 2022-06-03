import sys

X = int(sys.stdin.readline())

line = 0
M = 0

while X > M:
    line += 1
    M += line

gap = M - X

if line % 2 == 0:
    top = line - gap
    under = gap + 1
else:
    top = gap + 1
    under = line - gap
    
print(f'{top}/{under}')