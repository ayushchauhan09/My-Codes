N = int(input())
x = list()
for i in range(1, 11):
    if N%i==0:
        x.append(i)
x = sorted(x)
print(x[-1])