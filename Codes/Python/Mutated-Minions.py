T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    count = 0
    b = list()
    for j in a:
        b.append(j+K)
    for k in b:
        if k%7==0:
            count += 1
    print(count)