from heapq import heappush, heappop
def solution(users, emoticons):
    # 이모티콘 구매 비용의 합이 일정 가격 이상이 된다면,
    # 이모티콘 구매를 모두 취소하고 이모티콘 플러스 서비스에 가입
    # 출력 : 플러스 서비스 가입자, 총가격

    # 로직 : 완전탐색해 케이스별 나눠 플러스고객 최댓값을 추출한다.
    # 1. 이모티콘 할인율이 유저의 비율보다 크면 살 마음이 있음
    # 2. 이모티콘 할인율로 이모티콘 가격이 바뀜.
    # 3. 살 수 있는 모든 이모티콘의 바뀐 가격의 총합이 유저 가격보다 높으면 플러스 가입한다 => 우선시.
    # 4. 가입하면 유저가 산 이모티콘은 모두 0으로 바뀜 즉, 안삼.

    # 순서 : 구해야하는 것.
    # 1. 이모티콘 할인율의 설정 => 이모티콘 별로 DFS for문을 돌려 할인율을 정해줌. (index활용)
    # 2. 유저 별로 이모티콘 바뀐 가격의 총합. => 유저 for문 내 이모티콘 for문
    # 3. 할인율을 어떻게 선택할거냐 ! 10%, 20%, 30%, 40%
    # 4. 이모티콘 할인율을 유저의 가장 큰 할인율에 맞춰 놓고 계산 했을 때,
    # 5. 바뀐 가격의 총합이 본인의 가격이 넘는 자가 의 최댓값을 찾는 할인율을 설정한다.
    answer = []
    emoticons = [[price, 0] for price in emoticons]
    DFS(users, emoticons, 0, answer)
    result = heappop(answer)
    return [-result[0], -result[1]]

def DFS(users, emoticons, emoidx, answer):
    if emoidx == len(emoticons):
        subscribe_price = [0, 0]  # 구독자 총가입수, 구매 총액
        for rate, limitprice in users:
            userbuyprice = 0
            for price, salerate in emoticons:
                if rate <= salerate:
                    userbuyprice += price * (100 - salerate) // 100
            if limitprice <= userbuyprice:
                subscribe_price[0] += 1
                userbuyprice = 0
            subscribe_price[1] += userbuyprice
        heappush(answer, [-subscribe_price[0], -subscribe_price[1]])

    else:
        for salerate in [10, 20, 30, 40]:
            emoticons[emoidx][1] = salerate
            DFS(users, emoticons, emoidx + 1, answer)

ans = solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]]	,[1300, 1500, 1600, 4900])
print(ans)