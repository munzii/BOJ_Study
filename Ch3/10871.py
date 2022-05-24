import sys

N, X = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

for n in range(N):
    if A[n] < X:
        print(A[n], end = " ")