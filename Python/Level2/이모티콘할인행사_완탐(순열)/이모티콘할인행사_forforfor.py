def solution(users, emoticons):
    answer = [0,0]
    discount = [[]]
    for _ in emoticons:
        next_discount = []
        for case in discount:
            for per in (10, 20, 30, 40):
                next_discount.append(case+[per])
        discount = next_discount

    for case in discount:
        result = [0,0]
        for user in users:
            user_price = 0
            for per, price in zip(case,emoticons):
                if per >= user[0]:
                    user_price += price*(100-per)/100
            if user_price >= user[1]:
                result[0] += 1
            else:
                result[1] += user_price
        if result > answer:
            answer = result

    return answer

ans = solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]]	,[1300, 1500, 1600, 4900])
print(ans)