import sys

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())

mul = list(str(A * B * C))

for i in range(10):
    print(mul.count(str(i)))