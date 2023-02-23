def solution(food):
    answer = ''
    temp = ''
    length = len(food)
    for f in range(1, length):
        count = int(food[f] // 2)
        while count > 0:
            answer += str(f)
            count -= 1
    answer2 = answer[::-1]
    answer += '0'+answer2
    return answer