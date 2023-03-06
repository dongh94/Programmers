def solution(wallpaper):
    answer = []

    N = len(wallpaper)  # x층
    M = len(wallpaper[0])  # y층
    min_x = min_y = min_x1 = min_y1 = 51
    max_x = max_y = max_x1 = max_y1 = 0
    for x in range(N):
        for y in range(M):
            if wallpaper[x][y] == "#":
                min_x = min(min_x, x)
                min_x1 = min(min_x1, x + 1)
                min_y = min(min_y, y)
                min_y1 = min(min_y1, y + 1)

                max_x = max(max_x, x)
                max_x1 = max(max_x1, x + 1)
                max_y = max(max_y, y)
                max_y1 = max(max_y1, y + 1)

    lux = min(min_x, min_x1)
    luy = min(min_y, min_y1)
    rdx = max(max_x, max_x1)
    rdy = max(max_y, max_y1)
    answer = [lux, luy, rdx, rdy]
    return answer