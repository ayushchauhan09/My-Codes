N = input()
def counter(string):
    count = 0
    for i in string:
        if i=='0' or i=='6' or i=='9':
            count += 6
        elif i=='1':
            count += 2
        elif i=='2' or i=='3' or i=='5':
            count += 5
        elif i=='4':
            count += 4
        elif i=='7':
            count += 3
        elif i=='8':
            count += 7
    return count
print(counter(N))