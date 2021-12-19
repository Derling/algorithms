import os


def solution_part1(nums, boards):
    board_statuses = make_boards_status(len(boards), len(boards[0][0]))


def make_boards_status(boards, dimension):
    return [
        [
            False for _ in range(dimension)
        ]
        for _ in range(boards)
    ]


def extract_bingo_boards(boards_str_lines):
    boards = []
    cur_board = []
    for line in boards_str_lines:
        stripped_line = line.strip()
        if not stripped_line:
            if cur_board:
                boards.append(cur_board)
            cur_board = []
        else:
            cur_row = [i for i in stripped_line.strip().split()]
            cur_board.append(cur_row)
    return boards


if __name__ == '__main__':
    input_path = os.path.join(os.path.dirname(__file__), 'input.txt')
    with open(input_path, 'r') as f:
        numbers = [i.strip() for i in f.readline().split(',')]
        bingo_boards = extract_bingo_boards(f.readlines())
        print(solution_part1(numbers, bingo_boards))
