import sys
def bfs(r, c, now_sum, board, N , visited_col):
    global min_sum
    if r == N:
        min_sum = min(min_sum, now_sum)
        return
    if now_sum > min_sum:
        return
    for i in range(N):
        if not visited_col[i]:
            visited_col[i] = True
            bfs(r+1, i, now_sum+board[r][c], board, N, visited_col)
            visited_col[i] = False

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))
    visited_col = [False] * N

    min_sum = sys.maxsize
    for c in range(N):
        bfs(0, c, 0, board, N, visited_col)

    print(min_sum)
