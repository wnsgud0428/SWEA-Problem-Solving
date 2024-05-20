from collections import deque


def rotate_counter_clockwise(deq, n):
    for _ in range(n):
        v = deq.popleft()
        deq.append(v)


T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    numbers = deque(numbers)

    rotate_counter_clockwise(numbers, M)

    print(f"#{test_case} {numbers[0]}")
