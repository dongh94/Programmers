def solution(maps):
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    answer = []
    N = len(maps) # 행
    M = len(maps[0]) # 열
    for r in range(N):
        for c in range(M):
            if maps[r][c] == "X": continue;
            BFS(maps, r, c)
    return answer

def BFS(maps, r, c):
    pass