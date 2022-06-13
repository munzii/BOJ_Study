import sys

N = int(sys.stdin.readline())
x = []

for i in range(N):
    x.append(int(sys.stdin.readline()))

for i in sorted(x):
    sys.stdout.write(str(i) + '\n')