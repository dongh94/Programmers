def solution(a, b, n):
    answer = 0

    while n >= a:
        x, y = divmod(n, a)
        n = n - (a * x) + (b * x)
        answer += b * x

    return answer