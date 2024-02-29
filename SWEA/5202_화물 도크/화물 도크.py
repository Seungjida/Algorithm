import sys

sys.stdin = open("input.txt", "r")

T = int(input())


def find(start, count):
    global max_count, now
    if start == 25:
        if max_count <= count:
            max_count = count
    else:
        for i in range(start, len(work)):
            if now in work[i]:
                for same in work[i]:
                    registers[same] = False
            for hubo in range(len(work[i])):
                if registers[work[i][hubo]]:
                    now = work[i][hubo]
                    count += 1
                find(i+1, count)
                # 점점 산으로 가요..
                count -= 1
                for same in work[i]:
                    registers[same] = True


for tc in range(1, T + 1):
    # 도크 사용 신청서 개수
    n = int(input())
    # 작업 시작시간과 종료시간
    work = [[] for _ in range(25)]
    for r in range(n):
        n, e = map(int, input().split())
        for t in range(n, e):
            work[t].append(r)
    print(work)
    # 끝나자마자 시작하는 거 무조건 넣어 2개할 수 있으니까
    # 작업 시간 짧은 거 넣어

    # 몇번째 신청서를 수락 가능한지
    registers = [True] * n
    max_count = 0
    now = -1
    find(0, 0)