import sys

N = int(sys.stdin.readline())
cnt = 0
X = N

while 1:
    a = N // 10
    b = N % 10
    N = (b * 10) + ((a + b) % 10)
    cnt += 1
    if N == X:
        break

print(cnt)