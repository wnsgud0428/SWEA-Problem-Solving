from collections import deque


class Node:
    def __init__(self, r=None, c=None):
        self.r = r
        self.c = c

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(start_node, board, visited):
    N = len(board)
    q = deque([start_node])
    visited[start_node.r][start_node.c] = True

    while q:
        v = q.popleft()
        for i in range(4):
            nr = v.r + dr[i]
            nc = v.c + dc[i]
            if (0 <= nr <= N - 1 and 0 <= nc <= N - 1
                    and (board[nr][nc] == 0 or board[nr][nc] == 3)):
                if not visited[nr][nc]:
                    q.append(Node(nr, nc))
                    visited[nr][nc] = True
                    if board[nr][nc] == 3:
                        return True

    return False


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    board = []
    for _ in range(N):
        board.append(list(map(int, input())))
    visited = [[False] * N for _ in range(N)]

    start = Node()
    for i in range(N):
        for j in range(N):
            if board[i][j] == 2:
                start.r = i
                start.c = j

    answer = -1
    if bfs(start, board, visited):
        answer = 1
    else:
        answer = 0

    print(f"#{test_case} {answer}")
