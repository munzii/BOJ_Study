import sys

N = int(sys.stdin.readline())
cnt = 0
x = 666

while True:
    if '666' in str(x):
        cnt += 1
    if cnt == N:
        print(x)
        break
    x += 1