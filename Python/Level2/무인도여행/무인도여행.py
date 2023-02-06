from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
def solution(maps):

    answer = []
    N = len(maps) # 행
    M = len(maps[0]) # 열
    visited = [[0]*M for _ in range(N)]
    for r in range(N):
        for c in range(M):
            if maps[r][c] == "X": continue;
            ans = BFS(maps, r, c, N, M, visited)
            if ans != 0:
                answer.append(ans)
    answer.sort()
    return answer

def BFS(maps, r, c, N, M, visited):
    Q = deque([(r, c)])
    num = 0

    while Q:
        sr, sc = Q.popleft()
        if visited[sr][sc] == 1: continue;
        visited[sr][sc] = 1
        for d in range(4):
            nr = sr + dr[d]
            nc = sc + dc[d]
            if nr < 0 or nr >= N or nc < 0 or nc >= M: continue;
            if maps[nr][nc] != "X" and visited[nr][nc] == 0:
                visited[nr][nc] = 1
                num += int(maps[nr][nc])
    return num