from itertools import combinations

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    A = [i for i in range(1, 12 + 1)]
    N, K = map(int, input().split())
    candidate = list(combinations(A, N))

    count = 0
    for one in candidate:
        if sum(one) == K:
            count += 1

    print(f"#{test_case} {count}")