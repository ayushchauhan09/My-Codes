T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    if K>N:
        print(N)
    else:
        print(N%K)