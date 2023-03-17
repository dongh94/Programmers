def solution(board):
    ROWS, COLS = len(board), len(board[0])

    directions = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1),
    ]
    def is_valid(r, c):
        if r < 0 or r >= ROWS or c < 0 or c >= COLS: return False
        if board[r][c] == "D": return False
        return True

    def gen_key(r, c): return f"{r}:{c}"

    res = -1

    seen = [[[False for _ in range(4)] for _ in range(COLS)] for _ in range(ROWS)]
    UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3

    def delta_to_index(dR, dC):
        if dR == 0 and dC == 1: return UP
        if dR == 0 and dC == -1: return DOWN
        if dR == 1 and dC == 0: return RIGHT
        if dR == -1 and dC == 0: return LEFT

    def bfs(init_r, init_c, seen):
        queue = [(init_r, init_c)]
        steps = 0

        while queue:
            length = len(queue)

            for _ in range(length):
                r, c = queue.pop(0)

                if board[r][c] == "G": return steps

                for dR, dC in directions:
                    index = delta_to_index(dR, dC)
                    new_r, new_c = r + dR, c + dC

                    if not is_valid(new_r, new_c): continue
                    if seen[new_r][new_c][index]: continue

                    seen[new_r][new_c][index] = True
                    while is_valid(new_r, new_c):
                        new_r += dR
                        new_c += dC
                    new_r -= dR
                    new_c -= dC
                    queue.append((new_r, new_c))

            steps += 1
        return -1

    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c] != "R": continue

            return bfs(r, c, seen)

    return res