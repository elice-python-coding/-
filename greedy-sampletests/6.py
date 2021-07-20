from collections import deque


def solution(food_times, k):
    a = deque(food_times)
    position_change = 0
    sum_1 = sum(food_times)
    if sum_1 <= k:
        return -1

    while k != -1:
        now = a[0]
        position_change += 1
        if now > 0:
            a[0] = a[0] - 1
            a.append(a.popleft())
            k -= 1
        else:
            a.append(a.popleft())
    ret = position_change % len(food_times)
    if ret == 0:
        return len(food_times)
    else:
        return ret