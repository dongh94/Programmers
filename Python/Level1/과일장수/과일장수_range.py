def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    # 1.
    # while len(score) >= m:
    #     answer += min(score[:m]) * m
    #     score = score[m:]

    # 2.
    # for i in range(len(score) // m):
    #     answer += score[m-1 + (i*m)] * m

    # 3.
    for i in range(m - 1, len(score), m):
        answer += score[i] * m
    return answer