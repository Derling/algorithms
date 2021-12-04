import os


def get_gamma(bit_map):
    gamma = ''
    for counts in bit_map.values():
        zero_count = counts['0']
        one_count = counts['1']
        gamma += '0' if zero_count > one_count else '1'
    return gamma


def get_epsilon(gamma):
    return ''.join(['0' if i == '1' else '1' for i in gamma])


def solution_part1(report):
    gamma_map = {i: {'0': 0, '1': 0} for i in range(len(report[0]))}
    for bits in report:
        for idx, bit in enumerate(bits):
            gamma_map[idx][bit] += 1
    gamma = get_gamma(gamma_map)
    epsilon = get_epsilon(gamma)
    return int(gamma, 2) * int(epsilon, 2)


if __name__ == '__main__':
    input_path = os.path.join(os.path.dirname(__file__), 'input.txt')
    with open(input_path, 'r') as f:
        diagnostic = [i.strip() for i in f.readlines()]
        print(solution_part1(diagnostic))
