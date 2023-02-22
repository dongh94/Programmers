def solution(k, score):
    answer = []
    # 일차순으로
    # score점수를
    # 명예의 전당이 비었으면 넣어주고
    # 정렬한다?
    # max ~ k번째 max 값을 찾아
    # 지정된 변수를 갱신하며
    # 최하위점수(k번째)를 그날그날 append한다.
    hall_of_fame = []
    for s in score:
        if len(hall_of_fame) < k:
            hall_of_fame.append(s)
            answer.append(min(hall_of_fame))
        else:

            if s > min(hall_of_fame):
                hall_of_fame[hall_of_fame.index(min(hall_of_fame))] = s
                answer.append(min(hall_of_fame))
            else:
                answer.append(min(hall_of_fame))
    return answer