def solution(s, skip, index):
    answer = ''
    for st in s:
        cnt = index - 1
        node = ord(st) - 97 + 1  # a => 0 다음거니까 + 1
        if node == 26:
            node = 0

        while cnt:
            for sk in skip:
                skipnode = ord(sk) - 97
                if node == skipnode and node < 25:
                    node += 1
                    break
                elif node == skipnode and node == 25:
                    node = 0
                    break
            else:
                if node < 25:
                    node += 1
                else:
                    node = 0
                cnt -= 1
        answer += chr(node + 97)
    return answer