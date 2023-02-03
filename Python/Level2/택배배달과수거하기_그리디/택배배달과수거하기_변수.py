def solution(cap, n, deliveries, pickups):
    # 그리디 : 최대한 실어서 멀리있는 것 부터 가져다주고 거기서 최대한 pickup해오는 것.
    # 즉, 반복적인 개념에서 최소를 찾을 수 있다.

    # 먼저 돌려 놓고 시작 ! 중요.
    # for문 돌리면서 각 변수를가지고 -1까지 허용하며 answer에 더해주면 끝.
    answer = 0
    deliveries = deliveries[::-1]
    pickups = pickups[::-1]

    deli = 0
    pick = 0
    for i in range(n):
        deli += deliveries[i]
        pick += pickups[i]

        while deli>0 or pick>0:
            deli -= cap
            pick -= cap
            answer += (n - i) * 2