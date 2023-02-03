from itertools import product


def solution(users, emoticons):
    answer = [0, 0]


    cases = list(product([10, 20, 30, 40], repeat = len(emoticons)))
    for case in cases:
        eplus = 0
        totalmoney = 0

        for user in users:
            money = 0
            for i in range(len(emoticons)):
                if case[i] >= user[0]:
                    money += emoticons[i]*(100-case[i])//100
            if money>=user[1]:
                eplus += 1
            else:
                totalmoney += money

        if eplus > answer[0]:
            answer = [eplus, totalmoney]
        elif eplus == answer[0]:
            if totalmoney>answer[1]:
                answer = [eplus, totalmoney]
    return answer

ans = solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]]	,[1300, 1500, 1600, 4900])
print(ans)