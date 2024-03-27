# 하나의 시작 정점에서 누적거리가 최소인 정점을 선택해 나가면서 최단 경로를 구하는 방식
import sys
from heapq import heappop, heappush

sys.stdin = open("d_input.txt", "r")

INF = int(1e9)  # 어엄청 큰 값을 일단 넣음(10억)

V, E = map(int, input().split())
start = 0  # 시작 노드 번호 (문제마다 다르겠징)

# 인접 리스트
graph = [[] for _ in range(V)]
# 누적 거리를 저장할 변수
distance = [INF] * V

# 간선 정보 저장
for _ in range(E):
    s, e, w = map(int, input().split())
    # 인접 리스트니까 두가지 데이터 리스트로 같이 저장
    graph[s].append([w, e])


def dijkstra(start):
    # 후보군, weight 기준으로 정렬
    pq = []

    # 시작점의 weight, node 번호를 한 번에 저장
    heappush(pq, (0, start))
    # 시작 노드 초기화, 방문했다는 것도 여기 값으로 알 수 있음
    distance[start] = 0

    while pq:
        # 최단 거리 노드에 대한 정보
        dist, now = heappop(pq)
    
        # 이미 저장되어 있는 요소 따짐
        # pq의 특성 때문에 미리 저장된 더 긴 거리들은 계속 저장되어 있음, 이를 걸러줘야 함
        # 더 짧은 거리로 갱신되었지만 힙에는 계속 남아있는 값들
        # now가 이미 더 짧은 거리로 온 적이 있다면 pass
        if distance[now] < dist:
            continue

        # now에서 인접한 다른 노드 확인
        for to in graph[now]:
            next_dist = to[0]
            next_node = to[1]

            # 누적 거리 계산
            new_dist = next_dist + dist
            
            # 새로 저장할 요소 따져서 거리가 길면 굳이 안 넣어
            # 바로 밑 코드에서 보면, 여기서 조건으로 인해 걸러지지 않으면 무조건 값 갱신(원래는 작은 값이 들어와야 함) & 힙 추가
            # 이미 더 짧은 거리로 '간' 경우 pass (자취를 저장하기가 힘듦)
            if new_dist >= distance[next_node]:
                continue

            # 누적 거리를 현재까지의 최단 거리로 '갱신'
            distance[next_node] = new_dist
            # next_node의 인접 노드들을 추가
            heappush(pq, (new_dist, next_node))

# 다익스트라 알고리즘 실행
dijkstra(0)

# 모든 노드로 가기 위한 최단 (누적)거리들 출력
for i in range(V):
    # 도달할 수 없는 경우, 무한 출력
    if distance[i] == INF:
        print("INF", end=' ')
    else:
        print(distance[i], end=' ')
