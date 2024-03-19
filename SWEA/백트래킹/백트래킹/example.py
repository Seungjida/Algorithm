import sys

li = [[1,5,3],[2,5,7],[5,3,5]]
chk = [False]*3
m = sys.maxsize

def backtracking(row, score):
	if row == 4: # 재귀함수를 마치는 조건
		if score < m:
			return
	for i in range(1,4):
		if chk[i] == false: # 백트래킹에서의 한정조건
			chk[i] = true
			backtracking(row+1, score + li[row][i])
			chk[i] = false
	return

backtracking(1,0)
print(m)