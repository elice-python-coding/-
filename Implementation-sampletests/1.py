import math
N = input()


sum1 = 0
sum2 = 0
for i in range(math.floor(len(N)/2)):
    sum1 += int(N[i])
for j in range(math.ceil(len(N)/2),len(N)):
    sum2 += int(N[j])
print(sum1, sum2)
if sum1 == sum2:
    print("LUCKY")
else:
    print("READY")