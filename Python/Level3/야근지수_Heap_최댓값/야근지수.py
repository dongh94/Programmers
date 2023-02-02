import heapq
def solution(n, works):
    answer = 0
    heap = []

    # heap 최대! 튜플/리스트 이용
    for work in works:
        heapq.heappush(heap, [-work, work])

    for _ in range(n):  # n번 동안 -1 할수 있으니
        temp = heapq.heappop(heap)
        temp[0] += 1
        temp[1] -= 1
        heapq.heappush(heap, temp)

        # 1.
        # max_v =max(works)
        # idx = works.index(max_v)
        # works[idx] -= 1
        # 2
        # works.sort()
        # works[-1] -= 1

    for i, j in heap:
        if j > 0: answer += j ** 2

    return answer