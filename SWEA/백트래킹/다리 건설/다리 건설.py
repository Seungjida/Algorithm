# import sys
# sys.stdin = open("algo2_sample_in.txt", "r")

def back_tracking(depth, cnt, cost):
    global max_cnt, min_cost
    # 경우를 따지는 중간에라도 예산을 초과하면 그 케이스는 가능하지 않는 것으므로 return 한다.
    if v < cost:
        return

    # 끝까지 다 봤으면
    if depth == n:
        # 예산을 만족하는지 따진다.
        if v >= cost:
            # 현재 구한 수가 예산 안이면
            # 지금까지의 최대 건설 가능 다리수와 비교하여 건설할 수 있는 최대 다리의 수를 업뎃한다
            if cnt > max_cnt:
                max_cnt = cnt
                # 건설 비용도 같이 업뎃한다
                min_cost = cost
            # 만약 지금까지의 최대 건설 가능 다리수와 지금 구한 건설 가능 다리 수가 같다면
            elif cnt == max_cnt:
                # 다리 수는 같으니까 나두고, 건설 비용은 더 작은 것으로 업뎃한다.
                min_cost = min(min_cost, cost)
        return
    
    # 건설 할 다리의 개수, 건설비를 바꿔 인자에 넣어주며 백트래킹을 한다.
    back_tracking(depth+1, cnt+1, cost+c[depth])
    back_tracking(depth+1, cnt, cost)

T = int(input())
for tc in range(1, T+1):
    # 섬의 수, 예산
    n, v = map(int, input().split())
    # 각각에 대한 건설비용
    c = list(map(int, input().split()))
    max_cnt = float('-inf')
    min_cost = float('inf')

    back_tracking(0,0,0)
    print(f'#{tc} {max_cnt} {min_cost}')