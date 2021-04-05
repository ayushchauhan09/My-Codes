T = int(input())
for _ in range(T):
    arr = list(map(int, input().split()))
    K = int(input())
    for i in range(9,-1,-1):
        if K >= arr[i]:
            K = K-arr[i]
        else:
            print(i+1)
            break