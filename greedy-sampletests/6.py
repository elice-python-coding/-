food_times = list(map(int, input().split()))
k = int(input())
position_change = -1
sum = 0
while k != 0:
    for i in food_times:
        sum += i
    if sum ==0:
        return -1
    now = food_times[0]
    position_change += 1
    if int(now) > 0:
        food_times[0] = food_times[0] - 1
        temp = food_times[0]
        del food_times[0]
        food_times.append(temp)
        k -= 1
        print(k, food_times)
    else:
        temp = food_times[0]
        del food_times[0]
        food_times.append(temp)


print(position_change//len(food_times),"end!")

#다시풀기