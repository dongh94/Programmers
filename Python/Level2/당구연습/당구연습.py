def solution(m, n, startX, startY, balls):
    answer = []
    for endX, endY in balls:
        # 벽에 맞는 경우(4가지)
        diff = float('inf')
        # 윗 벽 ()
        if not (startX == endX and startY > endY):
            diff = min(diff, abs(startX - endX) ** 2 + (startY + endY) ** 2)
            print(diff)
        # 아래벽
        if not (startX == endX and startY < endY):
            diff = min(diff, abs(startX - endX) ** 2 + (2 * n - startY - endY) ** 2)
        # 왼 벽
        if not (startY == endY and startX > endX):
            diff = min(diff, (startX + endX) ** 2 + abs(startY - endY) ** 2)
        # 오른 벽
        if not (startY == endY and startX < endX):
            diff = min(diff, (2 * m - startX - endX) ** 2 + abs(startY - endY) ** 2)

        answer.append(diff)
    return answer

ans = solution(10, 10, 3, 7, [[7,7]])
print(ans)