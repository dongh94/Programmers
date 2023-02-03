def solution(cap, n, deliveries, pickups):
    answer = 0
    # 순서! , 우선 리스트자체를 소거하면서 진행하기 위해 deli와 pick을 계속 while시켜준다.
    # 소거이후, answer에 값을 추가하고 (deli와 pick의 가장 먼 길이를 2배 (왔다갔다))
    # 이후, cap을 차감하는 로직을 돌려준다.
    while deliveries or pickups:
        while deliveries and deliveries[-1] == 0:
            del deliveries[-1]
        while pickups and pickups[-1] == 0:
            del pickups[-1]
        answer += 2 * max(len(deliveries), len(pickups))

        # cap이 더 클땐, deli를 0으로 만들고,
        # 작을 땐 deli에서 빼주며 break한다. => cap이 없으므로
        can_del = cap
        for idx in reversed(range(len(deliveries))):
            if can_del < deliveries[idx]:
                deliveries[idx] -= can_del
                break
            else:
                can_del -= deliveries[idx]
                deliveries[idx] = 0

        # pick 도 마찬가지다.
        can_pku = cap
        for idx in reversed(range(len(pickups))):
            if can_pku < pickups[idx]:
                pickups[idx] -= can_pku
                break
            else:
                can_pku -= pickups[idx]
                pickups[idx] = 0

    return answer