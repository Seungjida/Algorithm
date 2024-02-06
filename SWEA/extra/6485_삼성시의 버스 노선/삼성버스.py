import sys
sys.stdin = open("s_input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    lines = [0 for _ in range(5001)]

    for i in range(n):
        a, b = map(int, input().split())
        for j in range(a,b+1):
            lines[j] += 1

    p = int(input())
    wondering_stops = [lines[int(input())] for k in range(p)]

    print(f'#{test_case} {" ".join(map(str, wondering_stops))}')