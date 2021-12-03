import os


def solution_part2(directions):
    aim = x = y = 0
    for d in directions:
        direction, units = d.split()
        units = int(units)
        if direction == 'forward':
            x += units
            y += aim * units
        elif direction == 'up':
            aim -= units
        else:
            aim += units
    return x * y


def solution_part1(directions):
    x = y = 0
    for d in directions:
        direction, units = d.split()
        units = int(units)
        if direction == 'forward':
            x += units
        elif direction == 'up':
            y -= units
        else:
            y += units
    return x * y


if __name__ == '__main__':
    input_path = os.path.join(os.path.dirname(__file__), 'input.txt')
    with open(input_path, 'r') as f:
        course = f.readlines()
        print(solution_part1(course))
        print(solution_part2(course))
