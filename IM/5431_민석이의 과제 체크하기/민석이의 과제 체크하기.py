import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    n, k = map(int, input().split())
    submit = list(map(int, input().split()))

    # do_not_submit = []
    # everyone = list(range(1, n+1))
    # for e in everyone:
    #     if e not in submit:
    #         do_not_submit.append(e)
    #
    # print(f'#{test_case} {" ".join(map(str,do_not_submit))}')

    student = [0] * (n+1)
    for i in submit:
        student[i] = 1

    print(f'#{test_case}', end=" ")
    for j in range(1, n+1):
        if student[j] == 0:
            print(student[j] , end=" ")
    print()