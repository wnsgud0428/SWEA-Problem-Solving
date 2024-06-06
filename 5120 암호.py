T = int(input())
for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())
    numbers = list(map(int, input().split()))

    # index = 0
    # for K번 반복:
    #     index 에 M만큼 추가
    #     list에 빈칸 삽입, 앞 뒤 더한 숫자 추가
    #     (%N 활용)

    index = 0
    for _ in range(K):
        index = (index + M) % len(numbers)
        if index == 0: index = len(numbers)
        numbers.insert(index, None)
        insert_value = numbers[(index - 1)] + numbers[(index + 1) % len(numbers)]
        numbers[index] = insert_value

    # print(numbers)
    print(f"#{test_case}", end=" ")
    if len(numbers) < 10:
        for e in numbers[::-1]:
            print(e, end = " ")
    elif len(numbers) >= 10:
        for i in range(10):
            print(numbers[len(numbers) - 1 - i], end=" ")
    print()
