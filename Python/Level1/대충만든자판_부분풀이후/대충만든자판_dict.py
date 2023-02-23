def solution(keymap, targets):
    answer = []
    keys_dict = {}
    for keys in keymap:
        idx = 1
        for key in keys:
            keys_dict[key] = min(keys_dict.get(key, idx), idx)
            idx += 1
    print(keys_dict)
    for target in targets:
        t_cnt = 0
        for t in target:
            if t in keys_dict.keys():
                t_cnt += keys_dict[t]
            else:
                t_cnt = -1
                break
        answer.append(t_cnt)
    return answer