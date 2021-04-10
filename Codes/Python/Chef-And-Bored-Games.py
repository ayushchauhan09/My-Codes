T = int(input())
for _ in range(T):
    N = int(input())
    count = 0
    if N%2==0:
        for i in range(2, N+1, 2):
            count += i**2
    else:
        for i in range(1, N+1, 2):
            count += i**2
    print(count)
