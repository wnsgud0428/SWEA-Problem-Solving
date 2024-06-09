from collections import deque


def bfs(root_node, tree: dict):
    q = deque()
    q.append(root_node)

    count = 0
    while q:
        v = q.popleft()
        count += 1
        for next in tree[v]:
            q.append(next)

    return count


T = int(input())
for test_case in range(1, T + 1):
    E, N = map(int, input().split())
    # 간선개수 E, 루트노드 N
    # 루트가 N인 subtree의 노드 개수 구하기
    info = list(map(int, input().split()))

    tree = dict()
    for i in range(1, E + 1 + 1):
        tree[i] = []

    for i in range(0, len(info), 2):
        parent = info[i]
        child = info[i + 1]
        tree[parent].append(child)
    # print(tree)

    answer = bfs(N, tree)
    print(f"#{test_case} {answer}")
