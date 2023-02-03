def solution(book_time):
    answer = 0
    time_table = [0 for _ in range(60 * 24 + 10)]
    for start, end in book_time:
        start_minutes = 60 * int(start[:2]) + int(start[3:])
        end_minutes = 60 * int(end[:2]) + int(end[3:]) + 10

        for i in range(start_minutes, end_minutes):
            time_table[i] += 1
    answer = max(time_table)
    return answer
