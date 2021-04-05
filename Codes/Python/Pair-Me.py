T = int(input())
for _ in range(T):
    x, y, z = map(int, input().split())
    if x+y==z or y+z==x or x+z==y:
        print("YES")
    else:
        print("NO")