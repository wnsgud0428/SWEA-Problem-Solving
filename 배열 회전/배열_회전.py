def rotate90(arr):
    N = len(arr)
    new_arr = [[None] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_arr[j][N - 1 - i] = arr[i][j]

    return new_arr


def rotate180(arr):
    N = len(arr)
    new_arr = [[] for _ in range(N)]
    for i in range(N):
        new_arr[N - 1 - i] = arr[i][::-1]

    return new_arr


def rotate270(arr):
    N = len(arr)
    new_arr = [[None] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_arr[N-1-j][i] = arr[i][j]

    return new_arr


arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
arr = rotate270(arr)
print(arr)
