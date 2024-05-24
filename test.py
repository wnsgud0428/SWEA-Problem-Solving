def bfs(si, sj):
    q = []
    v = [[0]*(N) for _ in range(N)]

    q.append((si,sj))
    v[si][sj]=1

    while q:
        ci,cj = q.pop(0)
        if arr[ci][cj]==3:  # 목적지에 도달한경우
            return v[ci][cj]-2

        # 4방향, 범위내이고, 미방문이고, 1이아니면(벽이 아닌경우)
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N and v[ni][nj]==0 and arr[ni][nj]!=1:
                q.append((ni,nj))
                v[ni][nj]=v[ci][cj]+1
    return 0                # 목적지에 도달하지 못한경우

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int,input())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j]==2:
                si, sj = i, j

    ans = bfs(si, sj)
    print(f'#{test_case} {ans}')