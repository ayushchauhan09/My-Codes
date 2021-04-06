T = int(input())
for _ in range(T):
    w1, w2, x1, x2, M = map(int, input().split())
    if w2 in range((M*x1)+w1, (M*x2)+w1+1):
        print(1)
    else:
        print(0)