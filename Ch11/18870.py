import sys

N = int(sys.stdin.readline())

A = list(map(int, sys.stdin.readline().split()))
B = sorted(list(set(A)))

X = {B[i]: i for i in range(len(B))}

for a in A:
    print(X[a], end = ' ')