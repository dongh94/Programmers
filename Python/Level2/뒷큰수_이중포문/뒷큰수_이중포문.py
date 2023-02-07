def solution(numbers):
    answer = []

    for i in range(len(numbers)):
        cnt = 0
        for j in range(i + 1, len(numbers)):
            if numbers[i] < numbers[j]:
                answer.append(numbers[j])
                cnt = 1
                break
        if cnt == 0:
            answer.append(-1)
    return answer