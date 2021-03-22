t = int(input())
for _ in range(t):
    a = int(input())
    fact = 1
    if a==0 or a==1:
        print(fact)
    else:
        for i in range(1, a+1):
            fact *= i
        print(fact)