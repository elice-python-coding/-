def solution(food_times, k):
    position_change = 0
    sum_1 = sum(food_times)
    if sum_1 <= k:
        return -1

    while k != -1:
        now = food_times[0]
        position_change += 1
        if now > 0:
            food_times[0] = food_times[0] - 1
            temp = food_times[0]
            del food_times[0]
            food_times.append(temp)
            k -= 1
        else:
            temp = food_times[0]
            del food_times[0]
            food_times.append(temp)
    ret = position_change % len(food_times)
    if ret == 0:
        return len(food_times)
    else:
        return ret