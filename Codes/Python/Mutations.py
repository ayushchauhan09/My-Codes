def mutate_string(string, position, character):
    a = list(string)
    b = str()
    a[position] = character
    for i in a:
        b += i
    return b
        

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)