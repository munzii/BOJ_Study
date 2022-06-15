import sys

N, M = map(int, sys.stdin.readline().split())

a = set()
for i in range(N):
    a.add(sys.stdin.readline().rstrip())
    
b = set()
for i in range(M):
    b.add(sys.stdin.readline().rstrip())
    
result = sorted(list(a & b))

print(len(result))

for name in result:
    print(name)