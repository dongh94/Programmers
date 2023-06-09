from collections import deque
from heapq import heappush, heappop


def solution(plans):
    answer = []
    sort_plans = []
    # 시간 초기화부터
    for plan in plans:
        name, start, playtime = plan
        a, b = map(int, start.split(":"))
        minu = a * 60 + b
        heappush(sort_plans, (minu, name, int(playtime)))
    print(sort_plans)

    left_stack = []
    while sort_plans:
        currentTask = heappop(sort_plans)
        name = currentTask[1]
        start = currentTask[0]
        playtime = currentTask[2]
        current_time = start

        if sort_plans:
            nextTask = sort_plans[0]
            next_start = nextTask[0]

            if current_time + playtime < next_start:
                answer.append(name)
                current_time += playtime

                while left_stack:
                    reTask = left_stack.pop()
                    re_name = reTask[0]
                    re_playtime = reTask[1]

                    if current_time + re_playtime <= next_start:
                        current_time += re_playtime
                        answer.append(re_name)
                        continue

                    else:
                        left_time = re_playtime - (next_start - current_time)
                        left_stack.append((re_name, left_time))
                        break
            elif current_time + playtime == next_start:
                answer.append(name)

            else:
                left_time = playtime - (next_start - current_time)
                left_stack.append((name, left_time))

        else:
            if not left_stack:
                current_time += playtime
                answer.append(name)
            else:
                answer.append(name)
                while left_stack:
                    reTask = left_stack.pop()
                    re_name = reTask[0]
                    answer.append(re_name)


    return answer