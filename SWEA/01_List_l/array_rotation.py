def rotation_90(n):
    rotation_shape = ''
    for i in range(N):
        rotation_shape += str(matrix[i][n])
    return rotation_shape[::-1]

def rotation_180(n):
    rotation_shape = ''
    for i in range(N):
        rotation_shape += str(matrix[(N-1)-n][i])
    return rotation_shape[::-1]

def rotation_270(n):
    rotation_shape = ''
    for i in range(N):
        rotation_shape += str(matrix[i][(N-1)-n])
    return rotation_shape

T = int(input())

for test_count in range(1, T+1):
    N = int(input())

    matrix = list()
    for input_count in range(N):
        matrix.append(list(map(int, input().split())))

    print(f'#{test_count}')

    for n_th in range(N):
        print(rotation_90(n_th), rotation_180(n_th), rotation_270(n_th))