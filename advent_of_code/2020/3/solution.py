from typing import List


def solution(tree_grid: List[List[str]], slope: tuple = (3, 1)):
    encounters = 0
    current_x, current_y = 0, 0
    grid_length = len(tree_grid[0])
    x, y = slope

    while(current_y != len(tree_grid) - 1):
        current_x, current_y = (current_x + x) % grid_length, current_y + y
        if tree_grid[current_y][current_x] == '#':
            encounters += 1

    return encounters

if __name__ == '__main__':
    import os
    fpath = os.path.join(os.path.dirname(__file__), 'input.txt')

    with open(fpath) as f:
        input_list = [line.strip() for line in f.readlines()]
        result = solution(input_list)
        print(f'part 1 answer is {result}')

        from functools import reduce
        part2_slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
        encounters = [solution(input_list, slope) for slope in part2_slopes]
        result = reduce(lambda p, n: p * n, encounters)
        print(f'part 2 answer is {result}')