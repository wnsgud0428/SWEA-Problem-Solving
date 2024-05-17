from collections import defaultdict, deque

def bfs(start, target, graph, visited):
    q = deque([start])
    visited[start] = True

    while q:
        v = q.popleft()
        for node in graph[v]:
            if not visited[node]:
                q.append(node)
                visited[node] = True
                if node == target:
                    return True

    return False

def dfs(start, graph, visited):
    visited[start] = True
    for node in graph[start]:
        if not visited[node]:
            dfs(node, graph, visited)


T = int(input())
for test_case in range(1, T + 1):

    graph = defaultdict(list)
    V, E = map(int, input().split())
    for _ in range(E):
        start, end = map(int, input().split())
        graph[start].append(end)
    # print(graph)

    S, G = map(int, input().split())
    # print(S, G)

    visited = [False] * (V + 1)

    answer = None
    dfs(S, graph, visited)
    if visited[G] == True:
        answer = 1
    else:
        answer = 0
    # print(visited)
    print(f"#{test_case} {answer}")