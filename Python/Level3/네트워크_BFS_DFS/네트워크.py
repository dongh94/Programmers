from collections import deque


def solution(n, computers):
    answer = 0

    computer_num = [0 for _ in range(n)]  # 컴퓨터 번호
    for i in range(n):  # 이 컴퓨터가 다른 컴퓨터와 연결이 된 건지 체크
        if not computer_num[i]:  # 연결 안됐으면
            DFS(n, computers, i, computer_num)  # 연결해 모두
            answer += 1  # 연결된 횟수 += 1

    return answer


def BFS(n, computers, i, computer_num):
    Q = deque([i])
    while Q:
        new_i = Q.popleft()
        computer_num[new_i] = 1  # 새 컴퓨터 연결
        for j in range(n):  # 중요! 새 컴퓨터를 찾아 (자신/이미연결 제외 1인거)
            if new_i != j and computers[new_i][j] == 1 and not computer_num[j]:
                Q.append(j)


def DFS(n, computers, i, computer_num):
    computer_num[i] = 1  # 새 컴퓨터 연결
    for j in range(n):  # 중요! 새 컴퓨터를 찾아 (자신/이미연결 제외 1인거)
        if i != j and computers[i][j] == 1 and not computer_num[j]:
            DFS(n, computers, j, computer_num)