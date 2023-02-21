from collections import deque


def solution(s):
    S = deque()
    for i in s:
        S.append(i)

    N = deque()
    answer = []
    while S:
        node = S.popleft()
        for n in range(len(N)):
            if node == N[n]:
                answer.append(n + 1)
                break
        else:
            answer.append(-1)
        N.appendleft(node)
    return answer