def solution(t, p):
    answer = 0

    t_length = len(t)
    p_length = len(p)
    p_int = int(p)
    for i in range(t_length - p_length + 1):
        if p_int >= int(t[i:i + p_length]):
            answer += 1

    return answer