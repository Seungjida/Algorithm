# 하나의 정점에서 연결된 간선들 중에 하나씩 선택해나가면서 MST를 만들어 나가는 방식
# 최소 비용의 간선이 존재하는 인접한 정점을 선택함
# 모든 정점이 선택될 때까지 반복
# bfs + 우선순위 큐

import sys
from heapq import heappop, heappush

sys.stdin = open("p_input.txt", "r")

def prim(start):
    heap = list()
    MST = [0] * V

    # 최소 비용 합계
    sum_weight = 0

    # 힙에서 관리해야 할 데이터
    # 갈 수 있는 후보들!
    # 가중치, 정점 정보
    heappush(heap, (0,start))

    while heap:
        # 우선순위 큐로 인해 가중치가 젤 작은 값이 맨 앞에 올 수밖에 없음
        # 간선을 지날 때 마다 비용이 증가하기 때문에 최소 간선 통과 + 그순간 최소 비용이 중요
        # 그래서 이미 선택된 정점은 최소 간선 통과 + 그 순간 최소 비용까지 만족한 찐 최소 비용
        weight, v = heappop(heap)

        # 이미 방문한 지점이면 통과
        # 무방향이라서 다시 돌아갈 수 있음(양방향 모두 저장) + 아직 방문 안 한 노드의 가중치보다 이미 값을 정한 노드의 남은 값?이 더 작을 수 있다
        if MST[v]:
            continue

        # 방문 처리 !!!!!!
        MST[v] = 1
        # 누적합 추가
        sum_weight += weight

        # 갈 수 있는 노드를 보면서
        for next in range(V):
            # 갈 수 없는 지점이면 continue
            if graph[v][next] == 0:
                continue

            # 이미 방문한 지점이면 continue
            if MST[next]:
                continue
            
            # 일단 후보들 다 때려 넣어
            heappush(heap, (graph[v][next], next))

    return sum_weight

V, E = map(int, input().split())
graph = [[0] * (V) for _ in range(V)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u][v] = w
    graph[v][u] = w  # 가중치가 있는 무방향 그래프

result = prim(0)
print(f'최소 비용 = {result}')