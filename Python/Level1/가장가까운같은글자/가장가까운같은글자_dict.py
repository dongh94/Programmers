# for문 순서대로 가면서 dict에 추가하면 같은 값이 갱신되면서 가장 큰 값을 추가시킬 수 있다.

def solution(s):
    answer = []
    dic = dict()
    for i in range(len(s)):
        if s[i] not in dic:
            answer.append(-1)
        else:
            answer.append(i - dic[s[i]])
        dic[s[i]] = i

    return answer