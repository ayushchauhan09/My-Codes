T = int(input())
for _ in range(T):
    N,B = map(int, input().split())
    tablet = list()
    for i in range(N):
        W,H,P = map(int, input().split())
        if P<=B:
            tablet.append(W*H)
    if len(tablet)==0:
        print("no tablet")
    else:
        print(max(tablet))