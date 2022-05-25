import sys

N = [int(sys.stdin.readline()) for _ in range(9)]

print(max(N))
print(N.index(max(N)) + 1)