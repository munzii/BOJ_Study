import sys

alp = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

T = sys.stdin.readline()

for i in alp:
    T = T.replace(i, '*')
    
print(len(T) - 1)