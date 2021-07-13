'''N시 59분 59초까지 3이 포함되어 있을 때의 경우의 수
    경우의 수가 86,400개이므로 100,000 즉 1초안에 해결이 될 수 있으므로,
    제한 시간 안에 해결할 수 있다.
    '''

# H를 입력받기
h = int(input())

count = 0
for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)
