from collections import deque


def solution(x, y, n):
    answer = 0
    answer = BFS(x, y, n)
    return answer


def BFS(x, y, n):
    Q = deque()
    Q.append((x, 0))

    while Q:
        node, cnt = Q.popleft()
        if node == y: return cnt
        if node + n > y: return -1

        for i in [n, 2, 3]:
            if i == n:
                if node + i > y: continue;
                new_node = node + i
                Q.append((new_node, cnt + 1))
            else:
                if node * i > y: continue;
                new_node = node * i
                Q.append((new_node, cnt + 1))
    return -1