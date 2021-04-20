T = int(input())
for _ in range(T):
    num = int(input())
    fact = 1
    if num==0 or num==1:
        print(fact)
    else:
        for i in range(1, num+1):
            fact *= i
        print(fact)