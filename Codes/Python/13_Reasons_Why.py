A, B, C = map(int, input().split())
temp = A
A = B
B = temp
A *= C
B += C
print(A, B)