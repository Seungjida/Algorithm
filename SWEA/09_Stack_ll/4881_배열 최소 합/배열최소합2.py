import sys
sys.stdin = open("sample_input.txt", "r")

def sum_check(line, total_line, hap):
    global min_sum
    if line == total_line:
        if hap < min_sum:
            min_sum = hap
    elif hap > min_sum:
        return
    else:
        for i in range(N):
            if not line_check[i]:
                line_check[i] = 1
                sum_check(line+1, total_line, hap+arr[line][i])
                line_check[i] = 0


T = int(input())

for test_case in range(1, T+1):
    # N * N 배열
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 입력 : N개 줄에 걸쳐 10보다 작은 자연수
    # => 해당 값보다 큰 수로 초기화
    min_sum = N * 10
    # 한 줄씩 더했는지 확인
    line_check = [0] * N

    sum_check(0, N, 0)
    print(f'#{test_case} {min_sum}')