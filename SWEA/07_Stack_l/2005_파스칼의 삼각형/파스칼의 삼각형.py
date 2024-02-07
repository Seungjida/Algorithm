# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    area = [[0]*n for _ in range(n)]

    print(f'#{test_case}')
    for i in range(n):
        for j in range(i+1):
            if j==0 or j==i:
                area[i][j] = 1
                print(area[i][j], end=' ')
            else:
                area[i][j] = area[i-1][j-1] + area[i-1][j]
                print(area[i][j], end=' ')
        print()