import heapq


class Task:
    def __init__(self, name, start, playtime):
        self.name = name
        self.start = start
        self.playtime = playtime

    def __lt__(self, other):
        return self.start < other.start


def solution(plans):
    answer = []
    pq = []

    for i in range(len(plans)):
        name = plans[i][0]
        h, m = map(int, plans[i][1].split(":"))
        start = h * 60 + m
        time = int(plans[i][2])
        pq.append(Task(name, start, time))

    pq.sort(key=lambda x: x.start)

    remaining_tasks = []

    while pq:
        current_task = heapq.heappop(pq)
        cur_name = current_task.name
        cur_start = current_task.start
        cur_playtime = current_task.playtime
        current_time = cur_start

        if pq:
            next_task = pq[0]

            if current_time + cur_playtime < next_task.start:
                answer.append(cur_name)
                current_time += cur_playtime

                while remaining_tasks:
                    rem = remaining_tasks.pop()

                    if current_time + rem.playtime <= next_task.start:
                        current_time += rem.playtime
                        answer.append(rem.name)
                        continue
                    else:
                        t = rem.playtime - (next_task.start - current_time)
                        remaining_tasks.append(Task(rem.name, t))
                        break
            elif cur_start + cur_playtime == next_task.start:
                answer.append(cur_name)
                continue
            else:
                t = next_task.start - current_time
                remaining_tasks.append(Task(cur_name, cur_playtime - t))
        else:
            if not remaining_tasks:
                current_time += cur_playtime
                answer.append(cur_name)
            else:
                answer.append(cur_name)
                while remaining_tasks:
                    rem = remaining_tasks.pop()
                    answer.append(rem.name)

    return answer
