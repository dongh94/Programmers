def solution(k, score):
    answer = []
    hall_of_fame = []
    for s in score:
        hall_of_fame.append(s)
        if (len(hall_of_fame) > k):
            hall_of_fame.remove(min(hall_of_fame))
        answer.append(min(hall_of_fame))

    return answer