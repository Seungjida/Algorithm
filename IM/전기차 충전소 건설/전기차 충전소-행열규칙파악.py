from itertools import combinations
import sys
sys.stdin = open("input.txt", "r")

T = int(input())

# 거리 구하는 함수
# 조건 만족하지 못 하면 0 반환하도록
def distance(x,y,h):
    minus = abs(x-h[0]) + abs(y-h[1])
    if 0 < minus <= h[2]:
        return minus
    return 0

for tc in range(1, T+1):
    n = int(input())
    # 집들의 위치
    homes = []

    # 충전소 후보
    # (x, y) : 몇 개의 집이 이 후보지에 세워도 가능한지
    locations = {}

    for _ in range(n):
        x, y, d = map(int, input().split())
        # 집 좌표와 거리 넣음
        homes.append([x, y, d])

        # + 모양이랑 곱하기 모양으로 델타 탐색해서 locations를 찾으려고 했는데 마름모가 아니라 꽃 모양처럼 나옴 왜그런지 다시 찾아보기
        # 그래서 집 좌표 기준으로 행의 차이를 활용해서 r을 선언하고 값 바꿈
        di = [1, -1]
        # 집 기준으로 -d ~ d까지의 row 가짐
        for r in range(-d, d + 1):
            # 그 행에 들어가면 중간 값 그러니까 집의 y값은 같고 x값이 양 옆으로 동시에 증가한다고 생각
            many = (d*2+1) - abs(r*2)

            # 집과 같은 x값과 행의 차이를 반영한 y값이 기준이 되어 양 옆으로 탐색할 거임
            ni = x
            nj = y - r
            if -15 <= ni <= 15 and -15 <= nj <= 15 and r!=0:
                if (ni, nj) in locations.keys():
                    locations[(ni, nj)] += 1
                else:
                    locations[(ni, nj)] = 1

            # x값을 바꾸며 후보가 될 수 있는 거 찾아서 locations에 저장
            for k in range(2 * (many//2)):
                ni = x + (di[k % 2] * (k // 2 + 1))
                if -15 <= ni <= 15 and -15 <= nj <= 15:
                    if (ni, nj) in locations.keys():
                        locations[(ni, nj)] += 1
                    else:
                        locations[(ni, nj)] = 1

    min_distance = 30 * n
    case = 0

    # 집은 후보가 될 수 없어
    # 다음 집의 후보 찾다가 또 전에 집 좌표를 넣었을 수도 있으니까
    # 딕셔너리에서 빼
    for h in homes:
        if tuple(h[:2]) in locations.keys():
            t = tuple(h[:2])
            del locations[t]

    # CASE 1
    # 충전소 후보 중에 모든 집이 도달할 수 있는 곳이 있다면
    for k,v in locations.items():
        # 만족하는 곳이 여러 개 일 수도 있으니까 locations를 다 탐색할 거임
        if v == n:
            case = 1
            dd = 0
            for h in homes:
                dd += distance(k[0], k[1], h)
            min_distance = min(dd, min_distance)

    # CASE 2
    if case != 1:
        # 후보지 중에 두 곳을 골라서 집과 그 후보지들의 거리가 조건을 만족하면,
        # 그 조건을 만족하는 것 중에 가장 작은 거리의 총 값을 구함
        hubo = combinations(locations.keys(), 2)
        for h in hubo:
            m_d = 0
            for home in homes:
                h0 = distance(h[0][0], h[0][1], home)
                h1 = distance(h[1][0], h[1][1], home)
                # 둘 다 0이상이면 둘 중에 더 작은 값
                if h0 > 0 and h1 > 0:
                    m_d += min(h0, h1)
                # 혹시나 둘 중 하나가 조건을 만족하지 못 해 0이 나올 수도 있음
                # 그러나 둘 중 하나만 조건을 만족하면 그 쪽 충전소에서 충전하면 되니까.. 그러면 더 큰 값
                elif h0 > 0 or h1 > 0:
                    m_d += max(h0, h1)
                # 둘 다 0이 나오면,, 그 후보지 2곳은 충전소를 설치할 수 없음
                # 후보지를 다시 뽑아
                else:
                    break
            # 모든 집들을 잘 순회했고 충전소와의 거리도 따졌다면..!
            # 그 후보지 2곳은 충전소가 될 수 있따능
            else:
                case = 2
                min_distance = min(m_d, min_distance)

    print(f'#{tc}', end=" ")
    if case == 0:
        print(-1)
    else:
        print(min_distance)