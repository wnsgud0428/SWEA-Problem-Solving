def returnPalindromeLength_inRow(board, string_length):
    N = len(board)
    for r in range(N):
        for i in range(0, N - string_length + 1):
            string = "".join(board[r][i:i + string_length])
            if isPalindrome(string):
                print(string)
                return len(string)

    return 0

def returnPalindromeLength_inCol(board, string_length):
    N = len(board)
    for c in range(N):
        string = ""
        for i in range(0, N - string_length + 1):
            for j in range(i, i + string_length):
                string += board[j][c]
            if isPalindrome(string):
                print(string)
                return len(string)

    return 0

def isPalindrome(string):
    n = len(string)
    for i in range(0, n // 2 -1 +1):
        if string[i] != string[n-1-i]:
            return False

    return True


if __name__ == '__main__':
    T = 1
    for _test_case in range(1, T + 1):
        tc = int(input())

        board = []
        for _ in range(100):
            board.append(list(input()))



        max_length = 0
        for string_length in range(100, 0, -1):
            max_length = max(returnPalindromeLength_inRow(board, string_length), max_length)
            max_length = max(returnPalindromeLength_inCol(board, string_length), max_length)

        print(max_length)
