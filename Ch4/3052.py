import sys

arr = []
for i in range(10):
    N = int(sys.stdin.readline())
    arr.append(N % 42)
    
arr = set(arr)
print(len(arr))