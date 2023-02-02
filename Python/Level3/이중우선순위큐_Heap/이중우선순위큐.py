def solution(operations):
    answer = []
    for oper in operations:
        if oper[0] == "I":
            num = int(oper[2:])
            answer.append(num)
        elif oper[0] == "D":
            num = int(oper[2:])
            if num == -1 and answer:
                idx = answer.index(min(answer))
                answer.pop(idx)
            elif num == 1 and answer:
                idx = answer.index(max(answer))
                answer.pop(idx)

    if not answer:
        answer = [0, 0]
    else:
        answer = [max(answer), min(answer)]

    return answer

print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))