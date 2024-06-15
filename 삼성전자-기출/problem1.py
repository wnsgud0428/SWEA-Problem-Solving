from collections import deque

dr3 = [-1, 0, 1, 0]  # 북동남서(시계방향)
dc3 = [0, 1, 0, -1]

dr2 = [-1, 1, 0, 0]  # 상하좌우
dc2 = [0, 0, -1, 1]
dr = {"up": -1, "down": 1, "left": 0, "right": 0}
dc = {"up": 0, "down": 0, "left": -1, "right": 1}


def printArr(arr):
    for i in range(len(arr)):
        print(arr[i])
    print("ㅡㅡㅡㅡㅡㅡㅡ")


class Golem:
    def __init__(self, r, c, exit, golem_num):
        self.r = r
        self.c = c
        self.exit = exit
        self.num = golem_num

    def goDown(self):
        self.r = self.r + dr["down"]
        self.c = self.c + dc["down"]

    def goLeftDown(self):
        self.r = self.r + dr["left"] + dr["down"]
        self.c = self.c + dc["left"] + dc["down"]
        # exit 회전
        self.exit -= 1
        if self.exit < 0:
            self.exit = 3

    def goRightDown(self):
        self.r = self.r + dr["right"] + dr["down"]
        self.c = self.c + dc["right"] + dc["down"]
        # exit 회전
        self.exit += 1
        if self.exit > 3:
            self.exit = 0

    def returnExitPosition(self):
        for i in range(4):
            if i == self.exit:
                nr = self.r + dr3[i]
                nc = self.c + dc3[i]
                return [nr, nc]

    def 출구회전(self):
        pass

    def canGoDown(self, board: list):
        m, n = len(board), len(board[0])
        checks = []
        checks.append((self.r + dr["down"] + dr["down"], self.c + dc["down"] + dc["down"]))
        checks.append((self.r + dr["down"] + dr["left"], self.c + dc["down"] + dc["left"]))
        checks.append((self.r + dr["down"] + dr["right"], self.c + dc["down"] + dc["right"]))

        for ch in checks:
            nr, nc = ch[0], ch[1]
            if not (0 <= nr <= m - 1 and 0 <= nc <= n - 1):
                return False
            if board[nr][nc] != 0:
                return False
        return True

    def canGoLeftDown(self, board: list):
        m, n = len(board), len(board[0])
        checks = []
        # 맨 위부터 시작
        pos_r = self.r + dr["left"] + dr["up"]
        pos_c = self.c + dc["left"] + dc["up"]
        checks.append((pos_r, pos_c))

        pos_r += dr["left"] + dr["down"]
        pos_c += dc["left"] + dc["down"]
        checks.append((pos_r, pos_c))

        pos_r += dr["down"]
        pos_c += dc["down"]
        checks.append((pos_r, pos_c))

        pos_r += dr["right"]
        pos_c += dc["right"]
        checks.append((pos_r, pos_c))

        pos_r += dr["down"]
        pos_c += dc["down"]
        checks.append((pos_r, pos_c))

        for ch in checks:
            nr, nc = ch[0], ch[1]
            if not (0 <= nr <= m - 1 and 0 <= nc <= n - 1):
                return False
            if board[nr][nc] != 0:
                return False
        return True

    def canGoRightDown(self, board: list):
        m, n = len(board), len(board[0])
        checks = []

        # 맨 위부터 시작
        pos_r = self.r + dr["right"] + dr["up"]
        pos_c = self.c + dc["right"] + dc["up"]
        checks.append((pos_r, pos_c))

        pos_r += dr["right"] + dr["down"]
        pos_c += dc["right"] + dc["down"]
        checks.append((pos_r, pos_c))

        pos_r += dr["down"]
        pos_c += dc["down"]
        checks.append((pos_r, pos_c))

        pos_r += dr["left"]
        pos_c += dc["left"]
        checks.append((pos_r, pos_c))

        pos_r += dr["down"]
        pos_c += dc["down"]
        checks.append((pos_r, pos_c))

        for ch in checks:
            nr, nc = ch[0], ch[1]
            if not (0 <= nr <= m - 1 and 0 <= nc <= n - 1):
                return False
            if board[nr][nc] != 0:
                return False
        return True


class Board:
    def __init__(self, r, c):  # board 위로
        self.r = r
        self.c = c
        info = [[0] * c for _ in range(r + 3)]
        self.info = info

    def board를_삐져나왔는가(self):
        for r in range(3):
            for c in range(self.c):
                if self.info[r][c] != 0:
                    return True

        return False

    def board_초기화(self):
        for i in range(self.r + 3):
            for j in range(self.c):
                self.info[i][j] = 0


R, C, K = map(int, input().split())
golems = []
for i in range(K):
    start_col, exit_info = map(int, input().split())
    golems.append(Golem(1, start_col - 1, exit_info, i + 1))

board = Board(R, C)
# print(board.info)

sum_of_max_row = 0
golem_save = dict()
for golem in golems:
    while golem.canGoDown(board.info) or golem.canGoLeftDown(board.info) or golem.canGoRightDown(board.info):
        if golem.canGoDown(board.info):
            golem.goDown()
        elif golem.canGoLeftDown(board.info):
            golem.goLeftDown()
        elif golem.canGoRightDown(board.info):
            golem.goRightDown()

    # print(golem.r, golem.c)
    # golem 정보에 맞게 board.info 수정
    board.info[golem.r][golem.c] = golem.num
    for i in range(4):
        nr = golem.r + dr2[i]
        nc = golem.c + dc2[i]
        board.info[nr][nc] = golem.num

    if board.board를_삐져나왔는가():
        board.board_초기화()
        # printArr(board.info)
        continue
    # printArr(board.info)

    golem_save[golem.num] = golem


    def 최하단_row_return():
        result = golem.r
        visited = [[False] * C for _ in range(R + 3)]
        q = deque()
        q.append(golem.num)

        while q:
            v = q.popleft()
            visited[golem_save[v].r][golem_save[v].c] = True
            for i in range(4):
                nr = golem_save[v].r + dr2[i]
                nc = golem_save[v].c + dc2[i]
                visited[nr][nc] = True
                result = max(result, nr)

            exit_pos = golem_save[v].returnExitPosition()
            for i in range(4):
                nr = exit_pos[0] + dr2[i]
                nc = exit_pos[1] + dc2[i]
                if 0 <= nr <= len(board.info) - 1 and 0 <= nc <= len(board.info[0]) - 1:
                    if board.info[nr][nc] != 0 and board.info[nr][nc] != v and not visited[nr][nc]:
                        q.append(board.info[nr][nc])

        return result




    most_down_row = 최하단_row_return() - 3 + 1
    sum_of_max_row += most_down_row
    # print(most_down_row)
    # printArr(can_go_map)
print(sum_of_max_row)
# for 골렘 in 모든_골렘:
#     while 골렘 갈수 있다면:
#         남쪽 이동
#         안되면, 서쪽으로 이동&출구회전
#         이것도 안되면, 동쪽으로 이동&출구회전
#     if 골렘이 board 삐져나오면:
#         board 비우기
#         continue (for문 다시 실행 -> 다음 골렘 시작)
#     정령 인접 이동 시키고(최하단 남쪽으로) -> 행 위치 누적
#
# def 정령_이동시키기:
#     q에 지금 골렘 번호 넣기
#     while q:
#         지금 골렘 상하좌우, 중간 visited 처리
#         if 출구쪽 상하좌우 검사 -> 지금 골렘 번호와 다른 골렘번호 있고, not visited 이면:
#             q에 추가
#
#     visited 배열의 최하단 row return 하기!