T = int(input())
for _ in range(T):
    N,K = map(int, input().split())
    arr = list(map(int, input().split()))
    arr2 = list()
    for i in arr:
        if i>K:
            arr2.append(K)
        else:
            arr2.append(i)
    print(sum(arr)-sum(arr2))