
def solution():
    x = input()
    alphabets = []
    num = 0
    for i in x:
        if 'A' <= i <= 'Z':
            alphabets.append(i)
        else:
            num += int(i)
    alphabets.sort()
    ret = "".join(alphabets) + "".join(str(num))
    return ret



print(solution())
