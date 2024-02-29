# import sys
#
# sys.stdin = open("sample_input.txt", "r")


def paint(start_line, end_line):
    global min_paint  # global 안 해도 상관없는거?

    if end_line > n - 2:
        return

    count = 0

    # 흰색
    for white_line in range(0, start_line):
        count += (m - colors[white_line][0])
    # 파란색
    for blue_line in range(start_line, end_line + 1):
        count += (m - colors[blue_line][1])
    # 빨간색
    for red_line in range(end_line + 1, n):
        count += (m - colors[red_line][2])

    min_paint = min(count, min_paint)
    paint(start_line, end_line + 1)


T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    colors = [[0, 0, 0] for _ in range(n)]

    for l in range(n):
        lines = input()
        for c in lines:
            if c == 'W':
                colors[l][0] += 1
            elif c == 'B':
                colors[l][1] += 1
            else:
                colors[l][2] += 1

    min_paint = n * m

    # 파란색이 어느 줄에 들어가고, 어느줄까지 파란색을 넣을 것이냐..
    for start in range(1, n - 1):
        paint(start, start)

    print(f'#{tc} {min_paint}')
