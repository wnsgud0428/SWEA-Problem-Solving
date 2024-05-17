T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    table = [[None] * 10 for _ in range(10)]


    def colorTable(r1, c1, r2, c2, color):
        for r in range(r1, r2 + 1):
            for c in range(c1, c2 + 1):
                if table[r][c] is None:
                    table[r][c] = color
                else:
                    if table[r][c] != color:
                        table[r][c] = 3  # 보라색은 3으로 설정 (빨강1, 파랑2)


    def countPurple():
        count = 0
        for r in range(len(table)):
            for c in range(len(table[0])):
                if table[r][c] == 3:
                    count += 1
        return count

    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        colorTable(r1, c1, r2, c2, color)

    purple_count = countPurple()

    print(f"#{test_case} {purple_count}")