def returnRcpWinner(a, b, cards):
    if cards[a] == cards[b]:
        return min(a, b)
    elif ((cards[a] == 1 and cards[b] == 2)
          or (cards[a] == 2 and cards[b] == 3)
          or (cards[a] == 3 and cards[b] == 1)):
        return b
    else:
        return a


def divideAndConquer(start, end, cards):
    if start == end:
        return start
    else:
        mid = (start + end) // 2
        a = divideAndConquer(start, mid, cards)
        b = divideAndConquer(mid + 1, end, cards)
        return returnRcpWinner(a, b, cards)


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    cards = list(map(int, input().split()))

    answer = divideAndConquer(0, N - 1, cards) + 1

    print(f"#{test_case} {answer}")
