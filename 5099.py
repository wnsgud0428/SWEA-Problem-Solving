from collections import deque


class Pizza:
    def __init__(self, number, cheese):
        self.number = number
        self.cheese = cheese
        self.rotate_count = 0


def isTherePizzaOnFire(fire):
    for p in fire:
        if p != None:
            return True
    return False


T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    cheese_amount = list(map(int, input().split()))

    pizzas = deque()
    for i in range(M):
        pizzas.append(Pizza(i + 1, cheese_amount[i]))

    done_pizza = []
    fire = deque([None] * N)
    fire[0] = pizzas.popleft()

    while isTherePizzaOnFire(fire):
        # 화덕 1번칸이 None 이면 피자 넣기
        if fire[0] == None and len(pizzas) > 0:
            fire[0] = pizzas.popleft()

        # 돌리기
        fire.rotate()
        for p in fire:
            if p != None:
                p.rotate_count += 1

        # 화덕 1번칸에 피자가 있으면?
        if fire[0] != None:
            # 피자가 한바퀴 돌았는지 체크
            if fire[0].rotate_count == N:
                fire[0].cheese //= 2
                fire[0].rotate_count = 0

            # 다 익었는지 체크
            if fire[0].cheese == 0:
                done_pizza.append(fire[0].number)
                fire[0] = None
                if len(pizzas) > 0:
                    fire[0] = pizzas.popleft()
    # if 빈칸 있으면: 넣기
    # 돌리기
    # 확인하기(치즈 다익었는지 -> 몇칸 돌았는지) -> 다 익었으면 빼기

    print(f"#{test_case} {done_pizza[-1]}")
