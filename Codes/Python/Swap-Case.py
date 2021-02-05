def swap_case(s):
    a = str()
    for i in s:
        if i == i.upper():
            a += i.lower()
        else:
            a += i.upper()
    return a
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)