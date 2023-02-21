def solution(t, p):
    answer = 0

    t_length = len(t)
    p_length = len(p)
    numlist = []
    for i in range(t_length - p_length + 1):
        numlist.append(int(t[i:i + p_length]))

    p_int = int(p)
    for n in numlist:
        if n <= p_int:
            answer += 1
    return answer