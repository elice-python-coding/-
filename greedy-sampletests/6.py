# food_times = list(map(int,input().split()))
# k = int(input())
# position_change = 0
# sum_1 = sum(food_times)
# if sum_1 <= k:
#     print(-1)
# i = 0
# length = len(food_times)
# while k != -1:
#     if i > length:
#         i = i % length - 1
#         print(i)
#     now = food_times[i]
#     print('now:',now)
#     if now > 0:
#         food_times[i] = food_times[i] - 1
#         k -= 1
#     i += 1
#     position_change += 1
#
#
# ret = position_change % length
# if ret == 0:
#     print(length)
# else:
#     print(ret)
#
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

##자료구조 마스터하고 풀것. 레벨4다..