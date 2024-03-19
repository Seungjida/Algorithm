import sys
sys.stdin = open("input.txt", "r")

def back_tracking(row, sum):
    global max_percentage
    if row == n:
        if sum > max_percentage:
            max_percentage = sum
        return

    for i in range(n):
        if visited[i] == 0 and p[row][i] != 0:
            visited[i] = 1
            sum *= p[row][i]
            back_tracking(row+1, sum)
            visited[i] = 0
            sum //= p[row][i]
    return

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    p = [list(map(int, input().split())) for _ in range(n)]
    visited = [0] * n

    max_percentage = 0
    back_tracking(0, 1)
    result = max_percentage / (100 ** (n - 1))  # 100의 (n-1) 제곱으로 나누기
    rounded_result = round(result, 6)  # 반올림하여 소수점 아래 6자리까지 정밀도 유지
    formatted_result = "{:.6f}".format(rounded_result)  # 문자열 포맷팅을 사용하여 소수점 아래 6자리까지 출력리까지 정밀도 유지

    print(f'#{tc} {formatted_result}')