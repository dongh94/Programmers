def solution(n):
    answer = ''
    while n > 0:
        q, r = divmod(n, 3)
        answer += str(r)
        n = q

    # return int(answer, base = 3)

    answer = answer[::-1]
    sum = 0
    for i in range(len(answer)):
        sum += int(answer[i]) * 3 ** i
    return sum