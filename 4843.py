from collections import deque

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))

    numbers.sort(reverse=True)
    numbers = deque(numbers)

    special_sort = []
    while numbers:
        special_sort.append(numbers.popleft())
        if numbers:
            special_sort.append(numbers.pop())
    # print(special_sort)

    print(f"#{test_case}", end = " ")
    for i in range(10):
        print(special_sort[i], end = " ")
    print()