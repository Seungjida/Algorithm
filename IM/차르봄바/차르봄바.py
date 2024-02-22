# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    n, p = map(int, input().split())
    virus = [list(map(int, input().split())) for _ in range(n)]

    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]

    max_remove = 0
    for i in range(n):
        for j in range(n):
            current_remove = virus[i][j]
            # 인덱스 조정인데 기준(di, dj)이 같고 그 기준에서 뭔가 조작(* ?)을 동시에 가하는 것임
            # 이중 반복문 자꾸 추가하지말고 변수 조작 시도 !
            for d in range(4 * p):
                ni = di[d % 4] * (d // 4 + 1) + i
                nj = dj[d % 4] * (d // 4 + 1) + j

                if 0 <= ni < n and 0 <= nj < n:
                    current_remove += virus[ni][nj]

            if current_remove > max_remove:
                max_remove = current_remove

    print(f'#{test_case} {max_remove}')
