import sys

N = int(sys.stdin.readline())

B = 0

while N >= 0:
    if N % 5 == 0:
        B += (N // 5)
        print(B)
        break
    N -= 3
    B += 1
else:
    print(-1)