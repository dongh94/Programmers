from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def solution(maps):
    answer = []
    N = len(maps)  # 행
    M = len(maps[0])  # 열
    visited = [[0] * M for _ in range(N)]
    for r in range(N):
        for c in range(M):
            if maps[r][c] == "X": continue;
            if visited[r][c] == 1: continue;
            ans = BFS(maps, r, c, N, M, visited)
            if ans != 0:
                answer.append(ans)
    if not answer:
        answer = [-1]
    answer.sort()
    return answer


def BFS(maps, r, c, N, M, visited):
    Q = deque([(r, c)])
    num = int(maps[r][c])

    while Q:
        sr, sc = Q.popleft()
        visited[sr][sc] = 1
        for d in range(4):
            nr = sr + dr[d]
            nc = sc + dc[d]
            if nr < 0 or nr >= N or nc < 0 or nc >= M: continue;
            if maps[nr][nc] != "X" and visited[nr][nc] == 0:
                visited[nr][nc] = 1
                num += int(maps[nr][nc])
                Q.append((nr, nc))

    return num