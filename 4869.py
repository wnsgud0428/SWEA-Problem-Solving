# 종이붙이기
from math import factorial

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    count = 0
    for i in range(0, N // 20 + 1):
        cnt_20 = i
        cnt_10 = (N - cnt_20 * 20) // 10
        # print(cnt_20, cnt_10)

        part_count = factorial(cnt_20 + cnt_10) // (factorial(cnt_20) * factorial(cnt_10))
        part_count *= 2 ** cnt_20
        count += part_count
    print(f"#{test_case} {count}")