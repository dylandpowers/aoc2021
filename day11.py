def total_flashes(board, steps):
    total = 0
    for _ in range(steps):
        should_flash = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 9:
                    should_flash.add((i, j))
                else:
                    board[i][j] += 1
        while should_flash:
            total += 1
            (i, j) = should_flash.pop()
            board[i][j] = 0
            for (x, y) in neighbors8(i, j, len(board), len(board[0])):
                # Only want to increment if it has not flashed this round
                if board[x][y] != 0 and (x, y) not in should_flash:
                    board[x][y] = (1 + board[x][y]) % 10
                    if board[x][y] == 0:
                        should_flash.add((x, y))
    return total


def first_step_all_flash(board):
    step = 0
    target = len(board) * len(board[0])
    while True:
        should_flash = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 9:
                    should_flash.add((i, j))
                else:
                    board[i][j] += 1
        flashes = 0
        while should_flash:
            flashes += 1
            (i, j) = should_flash.pop()
            board[i][j] = 0
            for (x, y) in neighbors8(i, j, len(board), len(board[0])):
                # Only want to increment if it has not flashed this round
                if board[x][y] != 0 and (x, y) not in should_flash:
                    board[x][y] = (1 + board[x][y]) % 10
                    if board[x][y] == 0:
                        should_flash.add((x, y))
        if flashes == target:
            return step + 1
        step += 1


def neighbors8(i, j, m, n):
    neighbors = [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1),
                 (i, j - 1), (i, j + 1),
                 (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)]

    return [(x, y) for (x, y) in neighbors if 0 <= x < m and 0 <= y < n]


def print_board(board):
    for line in board:
        print(line)


if __name__ == '__main__':
    with open('inputs/day11.txt') as f:
        data = [[int(x) for x in line.strip()] for line in f.readlines()]
    # print(total_flashes(data, 100))
    print(first_step_all_flash(data))
