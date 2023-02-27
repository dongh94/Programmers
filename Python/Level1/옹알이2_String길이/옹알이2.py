def ok(babbling):
    b = ''
    check = ''
    for string in babbling:
        b += string
        if len(b) == 2 or len(b) == 3:
            if b == "ye" and check != "ye":
                check = "ye"
                b = ''

            elif b == "ma" and check != "ma":
                check = "ma"
                b = ''

            elif b == "aya" and check != "aya":
                check = "aya"
                b = ''

            elif b == "woo" and check != "woo":
                check = "woo"
                b = ''

        elif len(b) > 3:
            return 0

    if b:
        return 0
    else:
        return 1


def solution(babbling):
    answer = 0
    for b in babbling:
        if ok(b):
            answer += 1
    return answer