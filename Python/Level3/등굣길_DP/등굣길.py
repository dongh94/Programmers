def solution(m, n, puddles):
    answer = 0
    # dp니까 첫값 0
    # 오른쪽으로 가거나 아래쪽으로 가니까
    # 다음 값은 위에서 내려오거나 왼쪽에서 온다. dp[i+1][j] / dp[i][j+1]

    dp = [[0]*m for _ in range(n)]
    for c, r in puddles:
        dp[r-1][c-1] = -1
    dp[0][0] = 1
    for i in range(n):
        for j in range(m):
            if dp[i][j] == -1 : dp[i][j] = 0; continue;
            if i > 0: dp[i][j] += dp[i-1][j] % 1000000007
            if j > 0: dp[i][j] += dp[i][j-1] % 1000000007
    answer = dp[n-1][m-1] % 1000000007 # dp 마지막 값도 큰 수 이므로 % 해줘야한다.
    return answer