def solution(book_time):
    # for 문 돌려서 숫자로 다시 넣고
    # 시작 시간 기준으로 sort해서
    # 조건에 안맞으면 check 갱신해서 answer += 1
    answer = 0
    books = []
    for start, end in book_time:
        starttime = int(start[:2]) * 60 + int(start[3:])
        endtime = int(end[:2]) * 60 + int(end[3:]) + 10
        books.append([starttime, endtime])
    books.sort(key=lambda x: x[0])

    reserved = []

    for i in range(len(books)):
        check = 0
        for j in range(len(reserved)):
            if reserved[j][1] > books[i][0]:
                check += 1
        if check == answer:
            answer += 1
        reserved.append(books[i])
    print(books)
    print(reserved)
    return answer

ans = solution([["00:00", "14:55"],["15:00", "17:00"], ["17:10", "23:59"]])
print(ans)