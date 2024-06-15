from 배열_회전 import rotate90, rotate180, rotate270


def portion_rotate90(arr, sr, sc, portion_length):
    # 부분 배열 복사 해오기: arr 부분 배열 -> portion_arr
    portion_arr = [[None] * portion_length for _ in range(portion_length)]
    for i in range(portion_length):
        for j in range(portion_length):
            # portion_arr[i][j] <- arr[sr + i][sc + j]
            portion_arr[i][j] = arr[sr + i][sc + j]

    # portion_arr 회전
    portion_arr = rotate90(portion_arr)

    # 다시 넣기: portion_arr -> arr 부분
    for i in range(portion_length):
        for j in range(portion_length):
            arr[sr + i][sc + j] = portion_arr[i][j]


N = 5
arr = [[N * j + i for i in range(1, N + 1)] for j in range(N)]
print(arr)
portion_rotate90(arr, 0,0,5)
print(arr)
