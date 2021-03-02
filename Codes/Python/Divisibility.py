N = int(input())
arr = list(map(int, input().split()))
if arr[-1] % 10 == 0:
    print('Yes')
else:
    print('No')