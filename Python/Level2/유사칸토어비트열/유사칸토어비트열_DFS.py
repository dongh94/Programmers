def solution(n, l, r):
    answer = DFS(n, l, r, 1)
    return answer
    # 11011
    # 11011 11011 00000 11011 11011
    # 11011 11011 00000 11011 11011 11011 11011 00000 11011 11011 00000
def DFS(n, l, r, idx):
    if n == 0: return 1

    ans = 0
    part = 5 ** (n-1)
    for i in range(5):
        if i == 2 or r < idx+part*i or (idx+part*(i+1) -1) < l: continue;
        ans += DFS(n-1, l, r, idx+part*i)
    return ans