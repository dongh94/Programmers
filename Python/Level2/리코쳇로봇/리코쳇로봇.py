from collections import deque

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
cnt = 0


def solution(board):
    answer = 0
    board_rowlength = len(board)
    board_collength = len(board[0])
    for r in range(board_rowlength):
        for c in range(board_collength):
            if board[r][c] == "R":
                answer = BFS(r, c, board, board_rowlength, board_collength)
    return answer


def BFS(r, c, board, board_rowlength, board_collength):
    Q = deque()
    Q.append((r, c))
    visited = [[0] * board_collength for _ in range(board_rowlength)]
    cnt = 0
    while Q:
        sr, sc = Q.popleft()
        if board[sr][sc] == "G":
            return visited[sr][sc]

        for d in range(4):
            nr = sr + dr[d]
            nc = sc + dc[d]
            if nr < 0 or nr >= board_rowlength or nc < 0 or nc >= board_collength:
                continue
            if board[nr][nc] == "." or board[nr][nc] == "G" and not visited[nr][nc]:
                visited[nr][nc] = visited[sr][sc] + 1
                Q.append((nr, nc))
            if board[nr][nc] == "D" and board[sr][sc] == "G":
                return cnt
    print(visited)
    return -1


def DFS(r, c, board, board_rowlength, board_collength, direct):
    global cnt
    if board[r][c] == "G":
        return cnt

    nr = sr + dr[direct]
    nc = sc + dc[direct]
    if nr < 0 or nr >= board_rowlength or nc < 0 or nc >= board_collength:
        continue
    if board[nr][nc] == ".":
        DFS(d)
    if board[nr][nc] == "." or board[nr][nc] == "G" and not visited[nr][nc]:
        visited[nr][nc] = visited[sr][sc] + 1
        Q.append((nr, nc))
    if board[nr][nc] == "D" and board[sr][sc] == "G":
        return cnt

