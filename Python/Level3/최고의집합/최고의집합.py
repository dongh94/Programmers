def solution(n, s):  # 2, 9
    answer = []
    # n개로 총합이 s가 되는 집합을 모두 찾기? ㄴㄴ
    # 그 곱 중 max인 집합을 배열(오름차순)? ㄴㄴ
    # -> 한번에 찾아 ! 곱이 큰거만 찾으면 된다는 것을 명심.
    # 주어진 s의 중간값 근처를 곱했을 때 가장 크다는 것을 확인.

    if n > s: return [-1];
    answer = [s // n] * n
    for i in range(s % n):
        answer[i] += 1
    answer.sort()
    return answer

print(solution(3, 13))
# def bestSet(n, s):
#     answer = []
#     a = int(s/n)
#
#     if a == 0:
#         return [-1]
#
#     b = s%n
#
#     for i in range(n-b):
#         answer.append(a)
#     for i in range(b):
#         answer.append(a+1)
#
#     return answer
#
# # 아래는 테스트로 출력해 보기 위한 코드입니다.
# print(bestSet(3,13))