import sys

sys.stdin = open("input.txt", "r")

def DFS(start_index):
    # 0에서 시작하니까 0부터 시작
    stack = [start_index]
    
    # stack이 비지 않았으니까 while문에 들어간다.
    # 만약 노드들을 다 순회하고 돌아오면 stack이 비니까 그땐 while문 종료
    while stack:
        # top의 요소 pop함
        now = stack.pop()
        # 만약 top의 요소가 99면 마지막에 도달한 거니까 1을 반환한다.
        if now == 99:
            return 1
        # 해당 노드에 인접한 노드가 있다면
        if arr[now]:
            # 방문한 노드의 인접한 노드 중에서 방문하지 않은 노드를 방문하며 stack에 추가한다.
            for adj in arr[now]:
                if visited[adj] is False:
                    stack.append(adj)
                    visited[adj] = True
    return 0


for _ in range(10):
    test_case, total_number = map(int, input().split())
    # 해당 노드를 인덱스라 치고 그 노드에 인접한 노드들을 요소로 넣을거임, 일단 빈 리스트로 넣어 놓는다
    arr = [[] for _ in range(100)]
    # 해당 노드를 방문한지 체크할 배열을 선언한다.
    visited = [False for _ in range(100)]
    # 방문한 노드를 넣을 스택을 만든다.
    stack = []
    
    # 데이터를 받는다
    input_data = list(map(int, input().split()))

    for i in range(0, len(input_data), 2):
      arr[input_data[i]].append(input_data[i + 1])

    # 데이터들을 두개씩 읽으며 앞에 것을 인덱스로 하고 그 인덱스에 요소로 뒤에 것을 추가한다.
    # for idx in range(total_number):
    #     arr[input_data[idx * 2]].append(input_data[idx * 2 + 1])

    print(f'#{test_case} {DFS(0)}')
