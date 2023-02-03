def solution(routes):
    # 모든 차량이 한 번은 단속용 카메라를 만나도록 하려면 최소 몇 대의 카메라

    # 정렬을 하면 그리디 규칙이 생기는 경우가 있다.
    # 진출기준 정렬해 지점에 카메라를 두고 진입보다
    answer = 0
    routes.sort(key=lambda x: x[1])
    camera = -30001

    for route in routes:
        if camera < route[0]:
            camera = route[1]
            answer += 1

    return answer

ans = solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]])
print(ans)