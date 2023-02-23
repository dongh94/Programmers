def solution(number, limit, power):
    answer = 0

    for i in range(1, number + 1):
        cnt = 0
        for j in range(1, int(i ** (1 / 2) + 1)): # 제곱근으로 반복횟수 줄이기.
            if i % j == 0:
                cnt += 1
                if j ** 2 != i: # 제곱근 값 빼고 나머지는 2번씩
                    cnt += 1
            if cnt > limit:
                cnt = power
                break
        answer += cnt

    return answer