from itertools import product
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = ' '.join(str(i) for i in product(A,B))
print(C)