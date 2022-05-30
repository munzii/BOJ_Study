import sys

S = sys.stdin.readline()
arr = list(range(97, 123))

for i in arr:
    print(S.find(chr(i)))