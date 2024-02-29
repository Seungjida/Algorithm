# import sys
#
# sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    # 도크 사용 신청서 개수
    n = int(input())
    # 작업 시작시간과 종료시간
    work = []
    for r in range(n):
        n, e = map(int, input().split())
        # 곧바로 이어서 작업시작가능하니까 굳이 e까지 안 넣음
        # 그리고 23~24시까지 작업하면 23에만 체크하면 되잖아
        work.append([n,e-1,e-n])
    # 작업시간이 작은 순서대로 픽하면 되는지.....왜 처음에 생각해놓고 또 못 함?
    work.sort(key=lambda x : x[2])

    working_time = [True] * 24
    count = 0
    for i in range(len(work)):
        start, end = work[i][0], work[i][1]
        for t in range(start, end+1):
            # 작업이 가능하면, 그 시간을 쓸 거니까 False로 만듦
            if working_time[t]:
                working_time[t] = False
            else:
                # 겹치는 시간 다시 되돌려야지
                for j in range(start, t):
                    working_time[j] = True
                break
        # for문이 잘 종료되면 작업이 진짜로 가능한 거니까 count ++
        else:
            count += 1
    print(f'#{tc} {count}')