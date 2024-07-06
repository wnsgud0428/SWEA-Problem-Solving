from collections import deque


def canArrive_bfs(start, end, graph, visited):
    q = deque()
    q.append(start)

    while q:
        v = q.popleft()
        for next in graph[v]:
            if not visited[next]:
                visited[next] = True
                q.append(next)
                if next == end:
                    return True

    return False


T = 10
for _test_case in range(1, T + 1):
    tc, edge = map(int, input().split())
    input_data = list(map(int, input().split()))
    graph = [[] for _ in range(100)]
    for i in range(0, edge * 2, 2):
        start = input_data[i]
        end = input_data[i + 1]
        graph[start].append(end)

    # print(graph)

    answer = 0
    visited = [False] * 100
    if canArrive_bfs(0, 99, graph, visited):
        answer = 1
    else:
        answer = 0

    print(f"#{tc} {answer}")
