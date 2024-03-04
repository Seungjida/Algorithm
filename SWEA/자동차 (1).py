from itertools import combinations
import sys
sys.stdin = open("input.txt", "r")

T = int(input())


def distance(x,y,h):
    minus = abs(x-h[0]) + abs(y-h[1])
    if 0 < minus <= h[2]:
        return minus
    return 0

for tc in range(1, T+1):
    n = int(input())
    # 집의 위치
    homes = []

    # 충전소 후보
    locations = {}

    # x,i가 col, y,j가 row임
    di_plus = [0,0,1,-1]
    dj_plus = [1,-1,0,0]

    di_mul = [1,1,-1,-1]
    dj_mul = [1,-1,1,-1]

    for _ in range(n):
        x, y, d = map(int, input().split())
        # change_x = x + 15
        # change_y = y - 15
        homes.append([x,y,d])

        # 일단 귀찮으니까 델타로 가능한 거 돌까
        for pl in range(4*d):
            ci = x + (di_plus[pl%4] * (pl//4 + 1))
            cj = y + (dj_plus[pl%4] * (pl//4 + 1))
            
            # 충전소 설치 가능 후보
            if -15 <= ci <= 15 and -15 <= cj <= 15 :
                if (ci, cj) in locations.keys():
                    locations[(ci, cj)] += 1
                else:
                    locations[(ci, cj)] = 1

        for mul in range(4 * (d-1)):
            ci = x + (di_mul[mul % 4] * (mul // 4 + 1))
            cj = y + (dj_mul[mul % 4] * (mul // 4 + 1))

            # 충전소 설치 가능 후보
            if -15 <= ci <= 15 and -15 <= cj <= 15:
                if (ci, cj) in locations.keys():
                    locations[(ci, cj)] += 1
                else:
                    locations[(ci, cj)] = 1

    min_distance = 30 * n
    case = 0

    for h in homes:
        if tuple(h[:2]) in locations.keys():
            t = tuple(h[:2])
            del locations[t]

    for k,v in locations.items():
        if v == n:
            case = 1
            dd = 0
            for h in homes:
                dd += distance(k[0], k[1], h)
            min_distance = min(dd, min_distance)

    if case != 1:
        hubo = combinations(locations.keys(), 2)
        for h in hubo:
            m_d = 0
            for home in homes:
                h0 = distance(h[0][0], h[0][1], home)
                h1 = distance(h[1][0], h[1][1], home)
                if h0 > 0 and h1 >0:
                    m_d += min(h0, h1)
                elif h0 > 0 or h1 > 0:
                    m_d += max(h0, h1)
                else:
                    break
            else:
                case = 2
                min_distance = min(m_d, min_distance)

    print(f'#{tc}', end=" ")
    if case == 0:
        print(-1)
    else:
        print(min_distance)