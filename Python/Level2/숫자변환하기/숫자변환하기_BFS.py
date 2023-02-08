from collections import deque


def solution(x, y, n):
    answer = 0
    answer = BFS(x, y, n)
    return answer

def BFS(x, y, n):
    Q = deque()
    Q.append((x, 0))
    visited = [0]*1000001
    visited[x] = 1
    while Q:
        node, cnt = Q.popleft()
        if node == y: return cnt
        if node > 10000000: return -1
        for i in range(1, 4):
            if i == 1:
                i = n
                if node + i > 1000000 or visited[node + n]: continue;
                new_node = node + i
                visited[new_node] = 1
                Q.append((new_node, cnt + 1))
            else:
                if node * i > 1000000 or visited[node * i]: continue;
                new_node = node * i
                visited[new_node] = 1
                Q.append((new_node, cnt + 1))
    return -1