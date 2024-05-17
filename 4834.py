
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    cards = list(map(int, input()))
    # print(cards)

    card_count = dict()
    for i in range(0,9+1):
        card_count[i] = 0

    for card in cards:
        card_count[card] += 1

    items = list(card_count.items())
    items.sort(key=lambda x: (-x[1], -x[0]))
    # print(items)

    print(f"#{test_case} {items[0][0]} {items[0][1]}")