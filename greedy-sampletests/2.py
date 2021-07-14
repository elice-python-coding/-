data= input()
result = 1
for i in data:
    if int(i) <= 1 or result <= 1:
        result += int(i)
    else:
        result *= int(i)

print(result)
