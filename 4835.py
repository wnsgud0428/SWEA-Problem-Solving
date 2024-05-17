T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    haps = []
    for i in range(0, N-(M-1)):
        haps.append(sum(numbers[i:i+M])) # O(M)

    print(f"#{test_case} {max(haps) - min(haps)}")