n = int(input())
data= list(map(int,input().split()))

data.sort()
print(data)

result = 1

for i in data:
    if result < i:
        break
    result += i

print(result)



