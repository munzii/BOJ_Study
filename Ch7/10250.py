import sys

T = int(sys.stdin.readline())

for i in range(T):
    H, W, N = map(int, sys.stdin.readline().split())
    num = N // H + 1
    F = N % H
    if N % H == 0:
        num = N // H
        F = H
    print(f'{F * 100 + num}')