'''
큰수의 법칙
배열의 크기  n
숫자가 더해지는 횟수 m
 연속으로 나올 수 있는 횟수k
배열 data
'''


n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort() #오름차순
first = data[n-1]
second = data[n-2]

result = 0

while True:
    for i in range(k): #k번만큼 가장 큰 수를 result에 담아준다
        if m == 0: # m 1씩 감소하여 0이 되면 for문 탈출
            break
        result += first
        m -= 1
    if m == 0: #for문이 끝나고 m이 0이면 while문 탈출
        break
    result += second #두번째로 큰 수 한번만 더하고 m 에서 1 빼기
    m -= 1

print(result)




