X, Y = map(float, input().split())
VAL = Y-X-0.50
if VAL>=0 and X%5==0:
    print(round(VAL, 2))
else:
    print(Y)