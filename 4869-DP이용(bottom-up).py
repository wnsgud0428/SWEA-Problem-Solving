# 4869-종이붙이기
# DP이용(bottom-up)
dp = [None] * 31  # N은 최대 300 -> 300//10

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    N = N // 10
    dp[1] = 1
    dp[2] = 3

    for i in range(3, N+1):
        if dp[i] == None:
            dp[i] = dp[i - 1] + 2 * dp[i - 2]

    print(f"#{test_case} {dp[N]}")