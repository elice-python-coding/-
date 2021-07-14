n = int(input())
depth, width = 1, 1
direction = input().split()
move_type = ['L','R','U','D']
#L R U D
d_depth = [0, 0, -1, 1]
d_width = [-1, 1, 0, 0]

for i in direction:
    for j in range(len(move_type)):
        if move_type[j] == i:
            temp_depth = depth + d_depth[j]
            temp_width = width + d_width[j]

    if temp_depth < 1 or temp_depth > n or temp_width < 1 or temp_width > n:
        continue
    depth, width = temp_depth, temp_width

print(depth, width)
