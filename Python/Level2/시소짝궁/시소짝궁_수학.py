def solution(weights):
    answer = 0
    # 1. 전체탐색하면 100000 * 100000 이므로 길다. 이중포문 안되고
    # 2. 리스트를 딕셔너리로 바꿔놓고 하자
    w_dict = dict()
    for w in weights:
        if w in w_dict:
            w_dict[w] += 1
        else:
            w_dict[w] = 1
    print(w_dict)

    ws = list(w_dict.keys())
    for i in range(len(ws)):
        for j in range(i, len(ws)):
            w1, w2 = ws[i], ws[j]
            if i == j and w_dict[w1] > 1:
                answer += w_dict[w1] * (w_dict[w1] - 1) // 2
                continue
            if w1 * 2 == w2 * 3:
                answer += w_dict[w1] * w_dict[w2]
            if w1 * 2 == w2 * 4:
                answer += w_dict[w1] * w_dict[w2]
            if w1 * 3 == w2 * 2:
                answer += w_dict[w1] * w_dict[w2]
            if w1 * 3 == w2 * 4:
                answer += w_dict[w1] * w_dict[w2]
            if w1 * 4 == w2 * 2:
                answer += w_dict[w1] * w_dict[w2]
            if w1 * 4 == w2 * 3:
                answer += w_dict[w1] * w_dict[w2]
    return answer


