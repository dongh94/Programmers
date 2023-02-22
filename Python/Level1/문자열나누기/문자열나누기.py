def solution(s):
    answer = 0

    low_alpha_dict = dict()
    last_idx = len(s) - 1
    idx = 0
    for alpha in s:
        low_alpha_dict[alpha] = low_alpha_dict.get(alpha, 0) + 1

        for key in low_alpha_dict.keys():
            if key != alpha and low_alpha_dict[alpha] == low_alpha_dict[key]:
                answer += 1
                print(low_alpha_dict)
                low_alpha_dict = dict()

                break
            elif idx == last_idx:
                answer += 1
                print(low_alpha_dict)
                break
        idx += 1

    return answer