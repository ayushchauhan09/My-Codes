T = int(input())
for _ in range(T):
    a = int(input())
    a = str(a)
    if a==a[::-1]:
        print("wins")
    else:
        print("loses")