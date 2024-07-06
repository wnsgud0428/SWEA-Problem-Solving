# <문제분석>
# 0보다 아래로 떨어지는 경우 암호문 생성 종료
#
# <생각>
# 앞에 원소를 때서 뒤에 붙여야 하므로 -> queue 사용

# <수도 코드>
# while 계속:
#     for n -> 1~5:
#         수열[0] n감소 -> 뒤로 보내기
#         만약 0보다 작으면! -> 모든 중첩 break (return 하면 될듯?)

from collections import deque


def encode(order: deque):
    while True:
        for n in range(1, 5 + 1):
            e = order.popleft()
            e -= n
            order.append(e)
            if order[-1] <= 0:
                order[-1] = 0
                return


T = 10
for _test_case in range(1, T + 1):
    tc = int(input())
    order = deque(map(int, input().split()))
    encode(order)

    print(f"#{tc} ", end="")
    for e in order:
        print(e, end=" ")
    print()
