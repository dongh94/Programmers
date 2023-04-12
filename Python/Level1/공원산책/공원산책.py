def solution(park, routes):
    answer = []
    d_dict = {"N": [-1, 0], "S": [1, 0], "W": [0, -1], "E": [0, 1]}
    r_len = len(park)
    c_len = len(park[0])
    sr = sc = 0

    for r in range(r_len):
        for c in range(c_len):
            if park[r][c] == "S":
                sr = r
                sc = c

    for route in routes:
        nr = sr
        nc = sc
        d, cnts = route.split()
        check = 0
        for _ in range(int(cnts)):
            cr = nr + d_dict[d][0]
            cc = nc + d_dict[d][1]
            # 범위
            if cr < 0 or cr >= r_len or cc < 0 or cc >= c_len or park[cr][cc] == "X":
                check = 1
                break
            nr = cr
            nc = cc

        if check == 1:
            check = 0
            nr = sr
            nc = sc
            continue;
        else:
            sr = nr
            sc = nc
    answer = [sr, sc]
    return answer