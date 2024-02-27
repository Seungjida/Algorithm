n = int(input())
# visited 같은 건데 row 배열의 값에 해당되는 것이 col
# row[] = col, row와 col 둘 다 봐야하니까, 그리고 인덱스가 0이 될 수도 있으니까 일단 -1로 잡음
row = [-1] * n
count = 0

def promising(x):
    # x는 이번에 col을 정할 row인데 그 앞에 결정된 row들을 돌면서 col 값이 겹치거나 대각선에 들어가지 않는지 확인해야 함
    # 대각선은 어떻게 확인하냐면 대각선이니까 어느 방향이든 절댓값을 씌우면 원래 값에서 1*?,1*?이 된다
    # 그럼 원래x - 비교x, 원래y - 비교y도 1*?, 1*?의 값이 되겠지
    # 그걸 이용해서 기존에 결정된 row(i)의 대각선에 놓일지 말지 결정한다.
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    return True

def backtracking(i):
    global count
    # 마지막 행까지 퀸의 위치를 정하면 count ++
    if i == n:
        count += 1
        return
    else:
        # 인자로 row의 위치는 정해졌고, 아래 for문을 통해 col의 위치를 정할 것임
        for j in range(n):
            # 일단 0~n-1을 순회하며 col의 값을 넣어
            # 조건에 안 맞으면 j를 바꾸며 조건의 맞는 col을 찾는다.
            row[i] = j
            # 해당 루트가 조건에 맞는지 검사!
            if promising(i):
                # 조건에 맞으면 다음 row의 col 값을 결정하러 간다.
                backtracking(i+1)
                row[i] = -1

backtracking(0)
print(count)