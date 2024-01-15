def row_non_overlapping():
    for row in range(9):
        if len(set(puzzle_data[row])) != 9:
            return False
    return True

def col_non_overlapping():
    # 조건이 조잡해서 나까지 헷갈림 ;; 잘 좀 적어봐라
    # 변수명 메이킹 연습 좀 해야할 듯..
    for col in range(9):
        col_elements_set = set()
        for row in range(9):
            col_elements_set.add(puzzle_data[row][col])
        if len(col_elements_set) != 9:
            return False
    return True

def grid_non_overlapping():
    for i in range(0,7,3):
        grid_elements_set = set()
        for row in range(3):
            for col in range(3):
                grid_elements_set.add(puzzle_data[row + i][col + i])
        if len(grid_elements_set) != 9:
            return False
    return True      

T = int(input())

for test_case in range(1, T+1):
    puzzle_data = list()
    for row in range(9):
        puzzle_data.append(list(map(int, input().split())))

    print(f'#{test_case}', end = ' ')

    if row_non_overlapping() and col_non_overlapping() and grid_non_overlapping():
        print('1')
    else:
        print('0')