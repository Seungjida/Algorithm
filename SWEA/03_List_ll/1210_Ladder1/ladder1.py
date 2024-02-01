import sys
sys.stdin = open("input.txt", "r")

END = 2
LADDER = 1

for _ in range(10):
    test_case = int(input())
    area = [list(map(int, input().split())) for _ in range(100)]

    # 현재 위치를 리스트에 넣음
    position = []
    # x의 위치를 일단 알아낸다!
    for col in range(100):
        if area[99][col] == END:
            position.extend((99, col))
            break

    # 끝에서부터 올라간다고 치면 밑으로 내려가는 일은 없으니까 그 경우 빼고 나머지 이동방향과 좌표를 딕셔너리에 넣음
    move = {'L': [0, -1], 'R': [0, 1], 'U':[-1, 0]}
    # 원래 가던 방향이 이어지면 계속 그 방향으로 가야하니까 (back 안 됨) pre_direction을 저장하는데 일단 up으로 둠
    pre_direction = 'U'

    # 0, ? 에 도착한 게 이제 처음 시작점이니까 거기를 찾아서 거슬러 올라가는 while문
    while position[0] > 0:
        # 가능한 이동 방향을 담은 리스트
        directions = []
        # 가능한 이동 좌표를 담은 리스트
        positions = []

        for direction, coordinate in move.items():
            # 현재 좌표에 L,R,U을 더한 새로운 좌표를 구함
            move_position = [position[0] + coordinate[0], position[1] + coordinate[1]]
            # 해당 좌표가 가능한 인덱스 영역이냐?
            if 0 <= move_position[0] <= 99 and 0 <= move_position[1] <= 99:
                # 가능한 인덱스 영역이라면 또 한 번 확인할 게 해당 좌표값이 레더 그러니까 1이냐
                if area[move_position[0]][move_position[1]] == LADDER:
                    # 1이면 이동이 가능한 후보니까 방향은 방향리스트에 좌표를 좌표리스트에 저장
                    directions.append(direction)
                    positions.append(move_position)

        # 만약 이전 방향이 UP 이었다면... 그냥 아무거나 와도 상관없으니까(빽이 불가능)
        # 맨 앞에 받은 가능한 이동방향과 좌표를 업데이트한다.(move 순서대로가면 L -> R -> U)
        if pre_direction == 'U':
            pre_direction = directions[0]
            position = positions[0].copy()
        # 만약 이전 방향이 L나 R이라면, 원래 진행중인 방향이 계속 진행가능하냐에 따라 확인해야 함
        else:
            # 만약 원래 진행방향이 있따? 그럼 그 진행방향 그대로 가고 좌표도 그만큼 감
            if pre_direction in directions:
                position = positions[directions.index(pre_direction)].copy()
            # 만약 원래 진행방향이 없다? 그러면 반대로 가면 안되니까 무조건 UP으로 가야함
            else:
                position = positions[directions.index('U')].copy()
                pre_direction = 'U'

    print(f'#{test_case} {position[1]}')