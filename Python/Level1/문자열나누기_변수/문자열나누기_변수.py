def solution(s):
    answer = 0
    target = ["", 0, 0]
    for alpha in s:
        if target[0] == "":
            target[0] = alpha
            target[1] += 1
        else :
            if target[0] == alpha:
                target[1] += 1
            else :
                target[2] += 1
            if target[1] == target[2]:
                answer += 1
                target = ["", 0, 0]
    if target != ["", 0, 0]:
        answer += 1
    return answer