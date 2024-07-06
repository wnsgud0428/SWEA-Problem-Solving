def n_power_m(n, m):
    if m == 0:
        return 1
    return n * n_power_m(n, m - 1)


T = 10
for _test_case in range(1, T + 1):
    tc = int(input())
    N, M = map(int, input().split())

    result = n_power_m(N, M)
    print(f"#{tc} {result}")
