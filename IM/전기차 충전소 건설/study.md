# 마름모 모양 탐색하기

1. 행과 열 사이의 규칙 찾아서 for문 잘 돌리기, 조건 잘 넣기
```python
for i in range(-d, d+1):
    for j in range(-d, d+1):
        if abs(i) + abs(j) <= d:
            nx, ny = x + i, y + j
```


2. 상하좌우로 기준을 바꿔가며 거기서 또 상하좌우 탐색

<img src='./마름모 탐색.png'>

```python
# visited 해주면 더 좋겠지
from collections import deque
di = [1,-1,0,0]
dj = [0,0,1,-1]

# 거리
d = 1
# 시작점은 나중에 알아서 빼기
start_x, start_y = -15, -15
# 위치만 ! 넣음, 일단 중복될 수도 있음
locations = []

# 기준 바꾸기
for i in range(4*d):
    now_xi = start_x + (di[i%4] * (i//4+1))
    now_yi = start_y + (dj[i%4] * (i//4+1))

    if 0 <= now_xi <= 30 and 0 <= now_yi <= 30:
        locations.append((now_xi, now_yi))
        
        # 그 기준에서 탐색
        for ii in range(4):
            next_xi = now_xi + di[ii]
            next_yi = now_yi + dj[ii]

            if 0 <= next_xi <= 30 and 0 <= next_yi <= 30:
                locations.append((next_xi, next_yi))

```

+) 거리가 d 이하를 만족하는 어쩌구~ 마름모 모양인가 생각!


## 시작 좌표가 (0,0)이 아닐 때
구하고 싶은 좌표값에서 배열의 시작 좌표를 빼주면, 원래 평소 생각하던 배열의 인덱스로 변환 가능

```python
def convert_coordinates_to_index(x, y):
    array_start_x, array_start_y = 15, 15  # 배열의 시작 좌표를 (0, 0)으로 바꿀 수 있는 상쇄값을 더해줌
    converted_x = x - array_start_x
    converted_y = y - array_start_y
    return converted_x, converted_y

# 예시: (-15, -15) 좌표를 배열 인덱스로 변환
converted_index = convert_coordinates_to_index(-15, -15)
print("Converted Index:", converted_index)

```