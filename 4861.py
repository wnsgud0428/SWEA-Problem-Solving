def isPalindrome(str):
    n = len(str)
    for i in range(n // 2):
        if str[i] != str[n - 1 - i]:
            return False
    return True


T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    # N: 보드 길이(N*N), M: 타겟 문자열 길이
    board = []
    for _ in range(N):
        board.append(list(input()))

    # print(board)


    def findPalindrome():
        for r in range(0, N):
            for c in range(0, N - (M - 1)):
                target = "".join(board[r][c:c + M])
                if isPalindrome(target):
                    return target
        return None


    find_str = ""
    find_str = findPalindrome()

    # 배열 뒤집어서 똑같이 찾기
    if find_str == None:
        board = list(map(list, zip(*board)))
        find_str = findPalindrome()

    print(f"#{test_case} {find_str}")