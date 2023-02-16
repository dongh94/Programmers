## %, // 를 활용

def check1(n):
    while n > 0:
        n, mod = divmod(n, 5)
        if mod == 2:
            return 0
    return 1

def solution(n, l, r):
    answer = 0
    for idx in range(l-1,r):
        answer += check1(idx)
    return answer