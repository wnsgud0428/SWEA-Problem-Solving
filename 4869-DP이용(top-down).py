# 4869-종이붙이기
# DP이용(top-down)
dp = [None] * 31  # N은 최대 300 -> 300//10
dp[1] = 1
dp[2] = 3

def initDp(n):
    if n==1 or n==2:
        return
    if dp[n - 1] == None:
        initDp(n - 1)
    if dp[n - 2] == None:
        initDp(n - 2)
    dp[n] = dp[n - 1] + 2 * dp[n - 2]

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    N = N // 10

    initDp(N)
    print(f"#{test_case} {dp[N]}")
