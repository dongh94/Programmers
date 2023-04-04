def solution(numbers, hand):
    answer = ""
    left, right = 10, 12
    for num in numbers:
        if num == 0:
            num = 11
        mod = num % 3
        if mod == 0:  # R
            answer += "R"
            right = num
        elif mod == 1:  # L
            answer += "L"
            left = num
        else:  # L or R
            minusL = num - left if num > left else left - num
            minusR = num - right if num > right else right - num
            distanceL = (minusL % 3) + (minusL // 3)
            distanceR = (minusR % 3) + (minusR // 3)
            if distanceL < distanceR:
                answer += "L"
                left = num
            elif distanceR < distanceL:
                answer += "R"
                right = num
            else:
                answer += "R" if hand == "right" else "L"
                if hand == "right":
                    right = num
                else:
                    left = num
    return answer