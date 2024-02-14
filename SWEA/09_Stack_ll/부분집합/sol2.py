def solution(arr, K, result):
    # 부분집합의 합이 10인 경우를 찾고 있다.
    # print(arr, result)
    if result != 10:
        return
    for i in range(1, K + 1):
        if arr[i]:
            print(data[i], end=' ')
    print()


def make_ncandidates(arr, K, N, c):
    c[0] = 1  # 쓸거임
    c[1] = 0  # 안쓸거임
    return 2  # 생각할 수 있는 경우의 수


def backtracking(arr, K, N, result):
    global count
    if result > 10:
        return
    count += 1
    # 총합 계산은 result로 진행
    # 후보군 목록
    c = [0] * 2  # 부분집합 원소 쓸래/말래 만 구분

    # 언제까지 조사 할거냐?
    # 현재 조사하는 위치가 최대 조사 상황에 도달할때까지
    if K == N:
        solution(arr, K, result)  # 값을 도출하는 함수 실행
    else:
        # 아직 사용해야 하는 원소들이 남았다면,
        # 사용할 원소 인덱스 1 증가
        K += 1
        # 내가 해당 원소를 쓸/말 결정하는 경우의 수 2개
        # 배열, 지금까지 사용한 원소 인덱스, 최대 원소 개수, 후보군 목록 배열
        ncandidates = make_ncandidates(arr, K, N, c)
        for i in range(ncandidates):  # 후보군 수 만큼 반복
            arr[K] = c[i]
            if arr[K]:  # K번쨰 원소 쓰기로 했으면
                # 총합에 원본 데이터의 K번째 원소의 값을 더해준다.
                backtracking(arr, K, N, result + data[K])
            else:  # 안쓰기로 했으면?
                # 지금 K번째 원소 쓰지는 않을거지만,
                # 다음 조사는 해야 한다. 대신, 안쓸거니까 총합에 안더하기
                backtracking(arr, K, N, result)


# 유망성 조사를 위한 변수
MAXCANDIDATES = 12  # 최대 후보군 수
NMAX = 12  # 최대 원소 수

count = 0
data = list(range(11))
arr = [0] * NMAX  # 각 원소를 사용할 것인지 체크할 배열

# 조사를 시작
# 체크할 배열, 시작점, 종료지점, 총합
backtracking(arr, 0, 10, 0)
print(count)
