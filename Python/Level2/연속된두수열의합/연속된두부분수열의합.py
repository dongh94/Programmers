def solution(sequence, k):
    lt = 0
    rt = 0
    ptr_len = float('inf')
    sum_val = 0
    answer = [0, 0]

    while rt < len(sequence) and lt <= rt:
        if lt == rt:
            sum_val = sequence[lt]

        if sum_val == k:
            # 범위 확인 후 answer
            if ptr_len > rt - lt + 1:
                ptr_len = rt - lt + 1
                answer[0] = lt
                answer[1] = rt

            sum_val -= sequence[lt]

            if rt < len(sequence) - 1:
                sum_val += sequence[rt + 1]

            if lt == rt:
                break

            lt += 1
            rt += 1

        elif sum_val > k:
            sum_val -= sequence[lt]
            lt += 1
        elif sum_val < k:
            if rt < len(sequence) - 1:
                sum_val += sequence[rt + 1]
            rt += 1

    return answer