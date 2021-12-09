import copy


def get_first_winning_board_score():
    with open('inputs/day4.txt') as f:
        numbers = [int(seq.strip()) for seq in f.readline().split(',')]
        f.readline()

        boards = []
        curr_board = []
        for line in f.readlines():
            if not line.strip():
                boards.append(curr_board)
                curr_board = []
            else:
                board_line = []
                for entry in list(filter(lambda x: x, line.split(' '))):
                    board_line.append(int(entry.strip()))
                curr_board.append(board_line)

        boards.append(curr_board)

    for num in numbers:
        for board in boards:
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == num:
                        board[i][j] = -board[i][j]
                        if has_won(board):
                            return sum_unmarked_cells(board) * num


def get_last_winning_board_score():
    with open('inputs/day4.txt') as f:
        numbers = [int(seq.strip()) for seq in f.readline().split(',')]
        f.readline()

        boards = []
        curr_board = []
        for line in f.readlines():
            if not line.strip():
                boards.append(curr_board)
                curr_board = []
            else:
                board_line = []
                for entry in list(filter(lambda x: x, line.split(' '))):
                    board_line.append(int(entry.strip()))
                curr_board.append(board_line)

        boards.append(curr_board)

    for num in numbers:
        next_boards = []
        for board in boards:
            should_append = True
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == num:
                        board[i][j] = -board[i][j]
                        if has_won(board):
                            should_append = False
                            if len(boards) == 1:
                                return sum_unmarked_cells(board) * num
            if should_append:
                next_boards.append(board)
        boards = next_boards


def has_won(board):
    # Rows
    for i in range(len(board)):
        j = 0
        while j < len(board[i]):
            if board[i][j] > 0:
                break
            j += 1
        if j == len(board[i]):
            return True

    # Columns
    for j in range(len(board[0])):
        i = 0
        while i < len(board):
            if board[i][j] > 0:
                break
            i += 1

        if i == len(board):
            return True

    return False


def sum_unmarked_cells(board):
    computed_sum = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            computed_sum += max(board[i][j], 0)
    return computed_sum
