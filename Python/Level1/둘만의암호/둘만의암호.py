def solution(s, skip, index):
    answer = ''
    for st in s:
        cnt = index
        node = ord(st) - 97  # a => 0

        while cnt:
            if node == 25:
                node = 0
            else:
                node += 1

            for sk in skip:
                skipnode = ord(sk) - 97
                if node == skipnode:
                    break
            else:
                cnt -= 1
        answer += chr(node + 97)
    return answer