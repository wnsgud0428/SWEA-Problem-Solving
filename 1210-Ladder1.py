# 상, 좌, 우
# dr = [-1, 0, 0]
# dc = [0, -1, 1]
dr = {"up": -1, "left": 0, "right": 0}
dc = {"up": 0, "left": -1, "right": 1}


class Node:
    def __str__(self):
        return f"({self.r}, {self.c})"

    def __init__(self, r, c):
        self.r = r
        self.c = c

    def goUp(self):
        self.r = self.r + dr["up"]
        self.c = self.c + dc["up"]

    def goLeft(self):
        self.r = self.r + dr["left"]
        self.c = self.c + dc["left"]

    def goRight(self):
        self.r = self.r + dr["right"]
        self.c = self.c + dc["right"]

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


T = 10
for test_case in range(1, T + 1):
    tc = int(input())
    board = []
    for _ in range(100):
        board.append(list(map(int, input().split())))


    # 2찾기 -> 역순으로 올라오기
    def find_start_node():
        r = 99
        for c in range(100):
            if board[r][c] == 2:
                return Node(r, c)
    node = find_start_node()
    # print(node)


    def search_ladder():
        while node.r > 0:
            node.goUp()
            if node.canGoLeft(board):
                node.goLeftMost(board)
            elif node.canGoRight(board):
                node.goRightMost(board)
    search_ladder()

    answer = node.c
    print(f"#{tc} {answer}")

    """ 
        while ㅁㅁ:
            올라오기
            if 왼쪽 or 오른쪽 만나면: 해당 방향으로 쭉!! 가기
            row가 0이 되면 종료 col return하기
        """
