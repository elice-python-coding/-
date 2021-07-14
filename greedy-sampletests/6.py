food_times = list(map(int, input().split()))
k = int(input())
position_change = 0
while k != 0:
    now = food_times[0]
    position_change += 1
    if now > 0:
        food_times[0] = food_times[0] - 1
        temp = food_times[0]
        del food_times[0]
        food_times.append(temp)
        k -= 1
        print(k)
    print('roll')
print(position_change//k)

#다시풀기