import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    str1 = input()
    str2 = input()

    print(f'#{test_case}', end=' ')
    if str1 in str2:
        print(1)
    else:
        print(0)
