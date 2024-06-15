# 상, 좌, 우
# dr = [-1, 0, 0]
# dc = [0, -1, 1]
dr = {"up": -1, "down": 1, "left": 0, "right": 0}
dc = {"up": 0, "down": 0, "left": -1, "right": 1}
N = 100  # N*N board


class Node:
    def __str__(self):
        return f"({self.r}, {self.c})"

    def __init__(self, r, c, start_number):
        self.r = r
        self.c = c
        self.start_number = start_number
        self.move_count = 0

    def goDown(self):
        self.r = self.r + dr["down"]
        self.c = self.c + dc["down"]
        self.move_count += 1

    def goLeft(self):
        self.r = self.r + dr["left"]
        self.c = self.c + dc["left"]
        self.move_count += 1

    def goRight(self):
        self.r = self.r + dr["right"]
        self.c = self.c + dc["right"]
        self.move_count += 1

    def canGoLeft(self, board: list):
        nr = self.r + dr["left"]
        nc = self.c + dc["left"]
        if 0 <= nr <= len(board) - 1 and 0 <= nc <= len(board[0]) - 1:
            if board[nr][nc] == 1:
                return True
        return False

    def canGoRight(self, board: list):
        nr = self.r + dr["right"]
        nc = self.c + dc["right"]
        if 0 <= nr <= len(board) - 1 and 0 <= nc <= len(board[0]) - 1:
            if board[nr][nc] == 1:
                return True
        return False

    def goLeftMost(self, board: list):
        while self.canGoLeft(board):
            self.goLeft()

    def goRightMost(self, board: list):
        while self.canGoRight(board):
            self.goRight()

    def isArrivedEnd(self, board: list):
        if self.r == len(board) - 1:
            return True
        return False


T = 10
for test_case in range(1, T + 1):
    tc = int(input())
    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))


    # 시작 지점들 찾기
    def return_start_col_numbers():
        start_col_numbers = []
        r = 0
        for c in range(N):
            if board[r][c] == 1:
                start_col_numbers.append(c)

        return start_col_numbers


    start_nodes = return_start_col_numbers()
    # print(start_nodes)

    result = []
    for i in start_nodes:
        node = Node(0, i, i)
        # 끝까지 내리기 -> 이동거리 result에 저장
        while not node.isArrivedEnd(board):
            node.goDown()
            if node.canGoLeft(board):
                node.goLeftMost(board)
            elif node.canGoRight(board):
                node.goRightMost(board)
        result.append([node.start_number, node.move_count])

    result.sort(key=lambda x: x[1])
    # print(result)

    answer = result[0][0]

    print(f"#{tc} {answer}")