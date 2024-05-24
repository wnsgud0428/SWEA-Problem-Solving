from collections import deque


class Node:
    def __init__(self, r, c):
        self.r = r
        self.c = c


def returnStartNode(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 2:
                return Node(i, j)


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(start_node, N, board, visited):
    distance = [[0] * N for _ in range(N)]
    q = deque([start_node])
    visited[start_node.r][start_node.c] = True

    while q:
        v = q.popleft()
        for i in range(4):
            nr = v.r + dr[i]
            nc = v.c + dc[i]
            # 1. 배열 벗어나지 않게
            if 0 <= nr <= N - 1 and 0 <= nc <= N - 1:
                # 2. 갈 수 있는 위치인지 확인(장애물이 없고, 방문하지 않은 곳만 갈 수 있음)
                if board[nr][nc] != 1 and not visited[nr][nc]:
                    distance[nr][nc] = distance[v.r][v.c] + 1
                    q.append(Node(nr, nc))
                    visited[nr][nc] = True
                    if board[nr][nc] == 3:
                        return distance[nr][nc] - 1
    # while q:
    #     v = q.popleft()
    #     if board[v.r][v.c] == 3:
    #         return distance[v.r][v.c] - 1
    #     for i in range(4):
    #         nr = v.r + dr[i]
    #         nc = v.c + dc[i]
    #         if 0 <= nr <= N - 1 and 0 <= nc <= N - 1:
    #             if board[nr][nc] != 1 and not visited[nr][nc]:
    #                 distance[nr][nc] = distance[v.r][v.c] + 1
    #                 visited[nr][nc] = True
    #                 q.append(Node(nr, nc))

    return 0


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    board = []
    for _ in range(N):
        board.append(list(map(int, input())))
    visited = [[False] * N for _ in range(N)]

    start_node = returnStartNode(board)
    answer = bfs(start_node, N, board, visited)
    print(f"#{test_case} {answer}")
