import sys

N = int(sys.stdin.readline())
T = list(map(int, sys.stdin.readline().split()))

print(min(T), max(T))