import sys

N = int(sys.stdin.readline())
result = 0

for i in range(1, N + 1):
    x = list(map(int, str(i)))
    result = i + sum(x)
    if result == N:
        print(i)
        break
    if i == N:
        print(0)