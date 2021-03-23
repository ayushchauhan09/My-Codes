T = int(input())
x = ['BattleShip','Cruiser','Destroyer','Frigate']
for _ in range(T):
    a = input()
    if a == 'b' or a == 'B':
        print(x[0])
    elif a == 'c' or a == 'C':
        print(x[1])
    elif a == 'd' or a == 'D':
        print(x[2])
    elif a == 'f' or a == 'F':
        print(x[3])