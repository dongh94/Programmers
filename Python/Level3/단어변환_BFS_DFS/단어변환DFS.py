
def solution(begin, target, words):
    answer = []
    if not target in words: return 0;
    word_length = len(words)
    begin_length = len(begin)
    cnt = 0
    visited = [0]* word_length # visited 방문표시 DFS용으로 만들고

    def DFS(begin, target, words, word_length, begin_length, cnt):
        nonlocal answer # DFS는 return 값을 갖는게 의미 없을 가능성이 크므로 전역을 사용한다. nonlocal
        if begin == target:
            answer = cnt
            return # return은 DFS선 거의 금물 계속 return 될수 없으니 전역을 사용한다.

        for i in range(word_length):
            if visited[i]: continue;
            word = words[i]
            same = 0
            for j in range(begin_length):
                if begin[j] == word[j]:
                    same += 1
            if same == begin_length - 1:
                visited[i] = 1
                DFS(word, target, words, word_length, begin_length, cnt + 1)
                visited[i] = 0

    DFS(begin, target, words, word_length, begin_length, cnt)
    return answer


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))