def solution(today, terms, privacies):
    answer = []
    Y, M, D = map(int, today.split("."))
    TOTAL = (Y * 12 * 28) + (M * 28) + D

    terms_dict = {}
    for term in terms:
        T, N = term.split()
        N = int(N) * 28
        terms_dict[T] = N

    idx = 0
    for privacy in privacies:
        idx += 1

        date, t = privacy.split()
        y1, m1, d1 = date.split(".")
        y, m, d = int(y1), int(m1), int(d1)
        totalday = (y * 12 * 28) + (m * 28) + d
        totalday += terms_dict[t]

        if TOTAL >= totalday:
            answer.append(idx)

    return answer