T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    sum = 0
    for i in arr:
        sum += i
    if sum%K == 0:
        print(0)
    else:
        print(1)