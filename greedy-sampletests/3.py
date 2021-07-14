data = input()
change = 0
stan = data[0]

for i in data:
    if i != stan:
        stan = i
        change += 1
        print('stan:',stan,'i:',i,'change:',change)
print(change // 2)
