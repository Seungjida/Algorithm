# 스택을 잘 몰랐어서 열심히 구현했습니다...!

OPEN_BRACKET = '('
CLOSE_BRACKET = ')'

def open_laser(i):
    if i+1 < len(brackets):
        if (brackets[i] == OPEN_BRACKET) and (brackets[i+1] == CLOSE_BRACKET):
            return True
    return False 

def closed_laser(i):
    if i-1 >= 0:
        if (brackets[i-1] == OPEN_BRACKET) and (brackets[i] == CLOSE_BRACKET):
            return True
    return False

brackets = list(input())
count_cut_piece = 0
iron_bar = 0

for i in range(len(brackets)):
    if brackets[i] == OPEN_BRACKET:
        if open_laser(i):
            count_cut_piece += iron_bar
        else:
            iron_bar += 1
    elif brackets[i] == CLOSE_BRACKET:
        if closed_laser(i):
            pass
        else:
            count_cut_piece += 1
            iron_bar -= 1

print(count_cut_piece)