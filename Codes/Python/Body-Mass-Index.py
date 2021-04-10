T = int(input())
for _ in range(T):
    M, H = map(int, input().split())
    B = M//H**2
    if B<=18:
        print(1)
    elif B in range(19, 25):
        print(2)
    elif B in range(25, 30):
        print(3)
    else:
        print(4)