# 전체!! 그래프를 보고, 가중치로 정렬한 다음, 가중치가 가장 작은 간선부터 뽑자

V, E = map(int, input().split())
edge = []
for _ in range(E):
    u, v, w = map(int, input().split())
    edge.append([u,v,w])
edge.sort(key=lambda x:x[2]) # 가중치 작은 거! 최소 비용!
parents = [i for i in range(V)]  # 대표 원소 배열

def find_set(x):
    if parents[x] == x:
        return x
    parents[x] = find_set(parents[x])
    return parents[x]

def union(x, y):
    x = find_set(x)
    y = find_set(y)

    if x==y:
        return

    # 더 작은 루트노드에 합친다(최소 간선 방문도 중요하니께?)
    if x < y:
        parents[y] = x
    else:
        parents[x] = y

# MST의 간선수 N = 정점수 - 1
# 선택한 edge의 수
cnt = 0
# MST 가중치의 합
total = 0
print(edge)
for u,v,w in edge:
    print(u,v,w)
    # 다른 집합이라면,
    if find_set(u) != find_set(v):
        cnt += 1
        union(u,v)
        total += w
        if cnt == V:
            break
print(f'최소비용 = {total}')