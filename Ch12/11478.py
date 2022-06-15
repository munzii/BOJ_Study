import sys

S = list(map(str, sys.stdin.readline().rstrip("\n")))
a = set()

for i in range(len(S)):
    for j in range(len(S) + 1):
        if S[i : j]:
            a.add("".join(S[i : j]))
        
print(len(a))