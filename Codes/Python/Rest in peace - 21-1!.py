T = int(input())
for _ in range(T):
    a = int(input())
    if a%21 == 0:
        print('The streak is broken!')
    else:
        if "21" in str(a):
            print('The streak is broken!')
        else:
            print('The streak lives still in our heart!')