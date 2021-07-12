'''어떠한 수 N이 1이 될 때까지 두 과정 중 하나를 반복적으로 선택하여 수행
    단, 두번째 연산은 N이 K 로 나누어 떨어질 때만 선택할 수 있다.'''

'''
    1.N에서 1을 뺀다
    2. N을 K로 나눈다.
    
    N과 K가 주어질 때 N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야 하는 최소 횟수를 구하는 프로그램을 작성하세오.
    '''
N, K = map(int, input().split())

count = 0
while N != 1:
    if N == 1: #탈출조건
        break
    if N % K == 0:
        N /= K
        count += 1
    else:
        N -= 1
        count += 1

print(count)



