
def insertAToTarget(target, A):
    for i, e in enumerate(target):
        if e > A[0]:
            target[i:i] = A
            return 0

    target.extend(A)
    return 0

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    input_sequences = []
    for _ in range(M):
        input_sequences.append(list(map(int, input().split())))

    # for 각수열 in 수열 2~끝 까지:
    #     수열1에 끼워넣기
    #     {각 수열[0] 보다 큰 숫자 찾기 -> 그 앞에 넣기
    #     없으면 -> 뒤에 추가}

    seq = input_sequences[0]
    for i in range(1, N):
        insertAToTarget(seq, input_sequences[i])

    print(f"#{test_case}", end = " ")
    for i in range(len(seq) - 1, len(seq) - 10 - 1, -1):
        print(seq[i], end=" ")
    print()
