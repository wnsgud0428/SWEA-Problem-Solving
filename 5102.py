from collections import defaultdict, deque


def bfs(start, target, graph, visited, distance):
    q = deque()
    q.append(start)
    visited[start] = True
    distance[start] = 0

    while q:
        v = q.popleft()
        for next in graph[v]:
            if not visited[next]:
                distance[next] = distance[v] + 1
                visited[next] = True
                q.append(next)
                if next == target:
                    return distance[next]

    return 0


T = int(input())
for test_case in range(1, T + 1):
    graph = defaultdict(list)

    V, E = map(int, input().split())
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    graph = dict(graph)
    S, G = map(int, input().split())

    visited = [False] * (V + 1)
    distance = [None] * (V + 1)

    answer = bfs(S, G, graph, visited, distance)
    print(f"#{test_case} {answer}")
    # print(graph)
