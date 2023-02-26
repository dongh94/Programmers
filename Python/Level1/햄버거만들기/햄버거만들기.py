def solution(ingredient):
    answer = 0

    bowl = [0] * 4
    for i in ingredient:
        if i == 1:
            if bowl[3] == 1:
                answer += 1
                bowl[1] -= 1
                bowl[2] -= 1
                bowl[3] -= 1
            else:
                bowl[1] += 1

        elif i == 2:
            if bowl[1] >= 1:
                bowl[2] += 1

        elif i == 3:
            if bowl[1] >= 1 and bowl[2] >= 1:
                bowl[3] += 1
        print(bowl)
    return answer