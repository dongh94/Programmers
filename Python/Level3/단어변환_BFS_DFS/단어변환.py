from collections import deque


def solution(begin, target, words):
    answer = 0
    # words 내부에 target이 없으면 바로 0 retrun
    if not target in words: return 0;
    # words 를 돌면서 begin과 비교했을때, 하나차이일때
    # 다음 기준으로 word를 선택해 리스트에 넣고
    # 리스트에 값을 다시 빼서 word를 찾는 과정을 반복하면서 count를 센다.
    # visited로 체크하고, visited[i] 값에 visited[i-1] + 1한다.
    # count가 가장 적게 나온 값을 return 한다.
    Q = deque([[begin, 0]])
    word_length = len(words)
    begin_length = len(begin)

    while Q:
        newword, cnt = Q.popleft()
        if newword == target: return cnt

        for i in range(word_length):
            word = words[i]
            same = 0
            for j in range(begin_length):
                if newword[j] == word[j]:
                    same += 1
            if same == begin_length - 1:
                Q.append([word, cnt + 1])