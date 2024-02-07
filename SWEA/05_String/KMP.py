def KMP(pattern, target):
    def make_lps():
        # 패턴을 "전처리"하여 잘못된 시작을 최소화 함
        # 내 앞에 나와 동일한 패턴이 몇번 나왔는지 세어주는 리스트
        lps = [0] * len(pattern)
        for idx in range(1, len(pattern)): # 0번 인덱스는 앞에 중복되는 값 없음
            # lps 배열은 pattern에서 해당 인덱스가 가진 값과 같은 값이 있는 곳의 인덱스를 가지고 있다.
            # pattern과 target이 같은 값이 나오기 전까지는 같은 값이 있는 곳의 인덱스를 모르니까 0을 가지고 있고 이는 pattern의 첫번째 값

            # 만약 pattern[0](젤 첫번째거 찾았다고 가정)과 같은 값을 가진 0 이후의 pattern 인덱스를 찾는다면
            if pattern[lps[idx-1]] == pattern[idx]:
                # 그 인덱스에 해당하는 lps 값을 전 인덱스 값 + 1 한다, 패턴 매칭에 실패했을 경우 돌아가는 위치
                # 그 전까지는 다 맞았으면 굳이 돌아갈 필요 없잖아
                lps[idx] = lps[idx - 1] + 1
        # 돌아갈 곳을 나타내는 값이 1이상이니까.........
        lps.insert(0, -1)
        return lps

    lps = make_lps()

    pattern_index = 0
    target_index = 0
    # 현재 조사위치가 조사대상의 범위를 벗어나기 전까지
    # print(lps)
    while target_index < len(target):
        # print(lps[pattern_index])
        # print(target_index, target[target_index], pattern_index, pattern[pattern_index])
        if pattern[pattern_index] != target[target_index]:
            pattern_index = lps[pattern_index]
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

for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    result = 0  # 들어있지 않다고 가정
    KMP(str1, str2)
    if str1 in str2:
        result = 1
    print(f'#{tc} {result}')
