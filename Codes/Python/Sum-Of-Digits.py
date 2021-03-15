T = int(input())
for _ in range(T):
    a = int(input())
    a = str(a)
    sum = 0
    for i in a:
        sum += int(i)
    print(sum)
