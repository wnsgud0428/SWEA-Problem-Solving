def binarySearch(start, end, target):
    count = 0
    while 1:
        mid = int((start + end) / 2)
        count += 1
        if target == mid:
            return count
        else:
            if mid < target:
                start = mid
            elif mid > target:
                end = mid



T = int(input())
for test_case in range(1, T + 1):
    P, A, B = map(int, input().split())
    a_count, b_count = binarySearch(1, P, A), binarySearch(1, P, B)

    answer = None
    if a_count > b_count:
        answer = "B"
    elif a_count == b_count:
        answer = 0
    elif a_count < b_count:
        answer = "A"

    print(f"#{test_case} {answer}")