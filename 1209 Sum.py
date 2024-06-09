def sum_row(row, board):
    hap = sum(board[row])
    return hap


def sum_col(col, board):
    hap = 0
    for r in range(100):
        hap += board[r][col]
    return hap


def sum_main_diagonal(board):
    hap = 0
    for i in range(100):
        hap += board[i][i]
    return hap


def sum_anti_diagonal(board):
    #  0 99 / 1 98 / 2 97
    hap = 0
    for i in range(100):
        hap += board[i][100 - 1 - i]
    return hap

T = 10
for test_case in range(1, T + 1):
    tc = int(input())
    board = []
    for i in range(100):
        board.append(list(map(int, input().split())))

    sum_list = []

    for r in range(100):
        sum_list.append(sum_row(r, board))
    for c in range(100):
        sum_list.append(sum_col(c, board))
    sum_list.append(sum_main_diagonal(board))
    sum_list.append(sum_anti_diagonal(board))

    answer = max(sum_list)
    print(f"#{test_case} {answer}")