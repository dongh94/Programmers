# def solution(ingredient):
#     answer = 0
#
#     bowl = [0] * 4
#     for i in ingredient:
#         if i == 1:
#             if bowl[3] == 1:
#                 answer += 1
#                 bowl[1] -= 1
#                 bowl[2] -= 1
#                 bowl[3] -= 1
#             else:
#                 bowl[1] += 1
#
#         elif i == 2:
#             if bowl[1] >= 1:
#                 bowl[2] += 1
#
#         elif i == 3:
#             if bowl[1] >= 1 and bowl[2] >= 1:
#                 bowl[3] += 1
#         print(bowl)
#     return answer

def solution(ingredient):
    answer = 0
    ingredient = ingredient + [0, 0]
    hamburger = [0] * 2
    for i in range(len(ingredient)):
        if ingredient[i] == 1:
            hamburger[0] += 1
        elif ingredient[i] == 2:
            if hamburger[0] >= 1 and ingredient[i + 1] == 3 and ingredient[i + 2] == 1:
                hamburger[0] -= 1
                ingredient[i + 1] = 0
                ingredient[i + 2] = 0
                answer += 1

    return answer