#import sys

#sys.stdin = open("sample_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    # 10 * 10 격자를 생성하고 0으로 초기화 함
    area = [[0] * 10 for _ in range(10)]
    purple = 0

    # 색칠 정보를 몇 번 받는지
    n = int(input())
    # 색칠할 범위와 색깔을 받는다
    for _ in range(n):
        *scope, color = list(map(int, input().split()))
        # 행에 대한 정보는 인덱스 0과 2에 있으니 이걸 범위로 순회한다.
        for row in range(scope[0], scope[2] + 1):
            # 열에 대한 정보는 인덱스 1과 3에 있으니 이걸 범위로 순회한다.
            for col in range(scope[1], scope[3] + 1):
                # 만약 해당 칸이 초기값이라면 방금 받은 값으로 칠한다.
                if area[row][col] == 0:
                    area[row][col] = color
                # 만약 해당 칸이 초기값과 방금 받은 값이 아니라면 겹쳐지는 칸이므로
                # purple ++
                elif area[row][col] != color:
                    purple += 1
    print(f'#{test_case} {purple}')
