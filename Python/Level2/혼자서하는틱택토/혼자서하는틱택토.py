def solution(board):
    bingoO = bingoX = cntO = cntX = 0

    for r in range(3):
        rowO = rowX = colO = colX = 0

        # 총 / 가로빙고 / 세로빙고 / 개수
        for c in range(3):
            if board[r][c] == "O":
                cntO += 1
                rowO += 1
            elif board[r][c] == "X":
                cntX += 1
                rowX += 1
            elif board[c][r] == "O":
                colO += 1
            elif board[c][r] == "X":
                colX += 1

        # 가로
        if rowO == 3:
            bingoO += 1
        elif rowX == 3:
            bingoX += 1

        # 세로
        elif colO == 3:
            bingoO += 1
        elif colX == 3:
            bingoX += 1

    crossO = crossX = cross2O = cross2X = 0
    for i in range(3):
        if board[i][i] == "O":
            crossO += 1
        elif board[i][i] == "X":
            crossX += 1
        elif board[2 - i][i] == "O":
            cross2O += 1
        elif board[2 - 1][i] == "X":
            corss2X += 1
    if crossO == 3 or cross2O == 3:
        bingoO += 1
    elif crossX == 3 or cross2X == 3:
        binogX += 1

    # 선공이 후공보다 적거나 2개 이상 많음
    if cntO < cntX or cntO >= cntX + 2:
        return 0

    # 둘다빙고
    if bingoO != 0 and bingoX != 0:
        return 0

    # 빙고가 2개보다 많음
    if bingoO + bingoX > 2:
        return 0

    # 승리시 O, X 갯수 같음
    if bingoO != 0 and cntO == cntX:
        return 0

    if bingoX != 0 and cntO > cntX:
        return 0

    return 1
