import sys

N = 19
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
move = [[1, 0], [1, 1], [0, 1], [-1, 1]]
result = 0

for i in range(N):
    for j in range(N):
        if board[i][j] != 0:
            stone = board[i][j]
            for dy, dx in move:
                ny, nx, cnt = i + dy, j + dx, 1
                while 0 <= ny < N and 0 <= nx < N and board[ny][nx] == stone:
                    cnt += 1
                    if cnt == 5:
                        if (0 <= i - dy < N and 0 <= j - dx < N and board[i - dy][j - dx] == stone) \
                            or (0 <= ny + dy < N and 0 <= nx + dx < N and board[ny + dy][nx + dx] == stone):
                            break
                        result = stone
                        y, x = i, j
                        break
                    ny += dy
                    nx += dx
    if result > 0:
        break

if result > 0:
    print(result)
    print(y + 1, x + 1)
else:
    print(0)
