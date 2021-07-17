data = input()


def solution(data):
    str_1 = ''
    stack = []
    count = 1
    stage = ''
    stage_compare = []
    ret = ''
    for i in range(1, len(data) + 1):
        for j in data:
            print('j:', j)
            if len(str_1) != i:
                str_1 += j
                print('if not len',str_1)
            else:
                stack.append(str_1)
                print('else', i, stack, str_1)
                str_1 = ''
                if len(stack) == 2:
                    if stack[0] == stack[1]:
                        count += 1
                        stack.pop()
                    else:
                        if count == 1:
                            stage += stack[0]
                            stack.clear()
                            print('if cleared stack',stack)
                            count = 1
                        else:
                            stage += str(count) + stack[0]
                            temp = stack[1]
                            stack.clear()
                            print('else cleared stack',stack)
                            stack.append(temp)
                            count = 1

        print(i, 'stage', stage)
        stage_compare.append(stage)
        stage = ''
    print(stage_compare)
    stage_min = 1000
    for k in stage_compare:
        if len(k) < stage_min:
            stage_min = len(k)
            ret = k
    return ret


print(solution(data))

######오답임