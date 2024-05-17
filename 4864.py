T = int(input())
for test_case in range(1, T + 1):
    str1 = input()
    str2 = input()

    answer = None
    if str1 in str2:
        answer = 1
    else:
        answer = 0

    print(f"#{test_case} {answer}")