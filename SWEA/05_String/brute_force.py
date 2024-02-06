'''
첫번째 방법: target_index를 검사한 부분으로 다시 돌려 그 다음 알파벳이랑 또 다시 조건을 따질 수 있게 한다.
그러니까 pattern의 일부분이라고 생각하고 넘겼던 인덱스들도 다시 돌아보며 보다 꼼꼼하게 살필 수 있다.
두번째 방법: target_index를 계속 +1 시켜 놓치는 부분이 있을 수 있다.
'''

def brute_force1(pattern, target):
    # 둘다 첫 조사 시작지점 0번에서 시작
    pattern_index = 0
    target_index = 0
    # 현재 조사위치가 조사대상의 범위를 벗어나기 전까지
    while target_index < len(target) and pattern_index < len(pattern):
        # 일치하지 않으면
        if pattern[pattern_index] != target[target_index]:
            # target_index가 이동한 만큼 같다고 생각한 부분이니까 다시 그만큼 back 하면 됨
            # line 16에서 ++하니까 같다고 생각한 그 다음 부분부터 조건 따짐
            target_index = target_index - pattern_index
            pattern_index = -1
        # 일치하면 => 사실상 항상
        target_index += 1
        pattern_index += 1

        # 패턴의 끝까지 index가 증가했다
        # -> target과 pattern이 일치하지 않는 부분 없이
        # 패턴의 끝까지 조사했다.
        if pattern_index == len(pattern):
            return True
    return False

def brute_force2(pattern, target):
    # 둘다 첫 조사 시작지점 0번에서 시작
    pattern_index = 0
    target_index = 0
    # 현재 조사위치가 조사대상의 범위를 벗어나기 전까지
    while target_index < len(target):
        # 일치하지 않으면
        if pattern[pattern_index] != target[target_index]:
            pattern_index = -1
        # 일치하면 => 사실상 항상
        target_index += 1
        pattern_index += 1

        # 패턴의 끝까지 index가 증가했다
        # -> target과 pattern이 일치하지 않는 부분 없이
        # 패턴의 끝까지 조사했다.
        if pattern_index == len(pattern):
            return True
    return False

T = int(input())
for tc in range(1, T + 1):
    str1 = input()
    str2 = input()
    result = 0  # 들어있지 않다고 가정
    # brute_force1(str1, str2)
    brute_force2(str1, str2)
    if str1 in str2:
        result = 1
    print(f'#{tc} {result}')
