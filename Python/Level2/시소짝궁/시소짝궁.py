def solution(weights):
    answer = 0
    check = [0] * 4001

    for i in range(len(weights)-1):
        check[weights[i]] = 1
        check[weights[i] * 2] = 1
        check[weights[i] * 3] = 1
        check[weights[i] * 4] = 1

        for j in range(i + 1, len(weights)):
            if check[weights[j]] or check[weights[j] * 2] or check[weights[j] * 3] or check[weights[j] * 4]:
                answer += 1
        check[weights[i]] = 0
        check[weights[i] * 2] = 0
        check[weights[i] * 3] = 0
        check[weights[i] * 4] = 0

    return answer