T = int(input())
for _ in range(T):
    N = int(input())
    count = 0
    count+=(N//100)
    N=N%100
    count+=N//50
    N=N%50
    count+=N//10
    N=N%10
    count+=N//5
    N=N%5
    count+=N//2
    N=N%2
    count+=N//1
    print(count)