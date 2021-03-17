T = int(input())
for _ in range(T):
    a, b, c = map(int, input().split())
    x = list()
    x.append(a)
    x.append(b)
    x.append(c)
    x = sorted(list(set(x)))
    print(x[1])