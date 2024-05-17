T = int(input())
for test_case in range(1, T + 1):
    K, N, M = map(int, input().split())
    charges = list(map(int, input().split()))

    can_charge = [False] * (N+1)
    can_charge[0] = True
    for c in charges:
        can_charge[c] = True

    energy = K
    pos = 0
    def canGoToNext():
        next_charge = None
        for i in range(pos+1, N+1):
            if can_charge[i]:
                next_charge = i
                break
        if next_charge == None:
            return False

        if next_charge - pos <= energy:
            return True
        else:
            return False

    count = 0
    while energy > 0:
        energy -= 1
        pos += 1
        if can_charge[pos]:
            if canGoToNext() or pos+energy >= N:
                pass
            else:
                energy = K
                count += 1

        if pos == N:
            break

    if pos >= N:
        print(f"#{test_case} {count}")
    else:
        print(f"#{test_case} 0")




    # print(f"#{test_case} {diff}")
