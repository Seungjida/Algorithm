import sys
sys.stdin = open("input.txt", "r")

def back_tracking(row, probability):
    global max_percentage

    # 모든 직원에게 일을 배분한 경우 최대 성공 확률 갱신
    if row == n:
        max_percentage = max(max_percentage, probability)
        return
    # 최대가 1이니까 곱할수록 작아짐. 현재 최대보다 작으면 작은 게 맞음
    if probability < max_percentage:
        return
    # 각 직원에게 일을 배분하는 경우 탐색
    for i in range(n):
        if not visited[i] and p[row][i] != 0:
            visited[i] = True
            back_tracking(row+1, probability * p[row][i] / 100.0)
            visited[i] = False

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    p = [list(map(int, input().split())) for _ in range(n)]

    visited = [False] * n
    max_percentage = 0.0

    back_tracking(0, 1.0)

    rounded_result = round(max_percentage * 100, 6)
    formatted_result = "{:.6f}".format(rounded_result)

    print(f'#{tc} {formatted_result}')
