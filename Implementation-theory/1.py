'''상하좌우
    n X n  의 공간을 부여받음
    1,1에서 출발'''
n = int(input())
direction = input().split()
x,y = 1,1
    # L  R  U  D
dx = [0,0,-1,1]
dy = [-1,1,0,0]
'''만약 move_type하나하나에 대한 조건을 걸어서 구현한다면 코드가 길어질 수도 있다. R일경우 n 보다 커지면~ '''
move_type = ['L','R','U','D']
for i in direction:
    for j in range(len(move_type)):
        if i == move_type[j]:
            nx = x + dx[j]
            ny = y + dy[j]
#공간 벗어나는 경우 , 매개변수 값으로 초기화 하지 않는다.
    if nx < 1 or ny < 1 or nx > n or ny >n:
        continue
    x, y = nx, ny
print(x,y)


