T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    # 접두사 합(Prefix Sum) 활용
    sum_value = 0
    prefix_sum = [0]
    for number in numbers:
        sum_value += number
        prefix_sum.append(sum_value)

    haps = []
    for i in range(M, N + 1):
        haps.append(prefix_sum[i] - prefix_sum[i - M])

    print(f"#{test_case} {max(haps) - min(haps)}")
