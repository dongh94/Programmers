def solution(triangle):
    answer = 0
    len_tr = len(triangle)
    dp = [[0] * len_tr for _ in range(len_tr)]
    dp[0][0] = triangle[0][0]

    # triangle[i][j]로 가는길은 triangle[i-1][j-1], triangle[i-1][j]이다.
    for i in range(len_tr - 1):
        for j in range(len(triangle[i])):
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + triangle[i + 1][j])
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + triangle[i + 1][j + 1])
    answer = max(dp[-1])
    return answer

result = solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])
print(result)
