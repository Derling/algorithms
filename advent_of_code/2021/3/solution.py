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


def get_gamma_map(data):
    gamma_map = {i: {'0': 0, '1': 0} for i in range(len(data[0]))}
    for bits in data:
        for idx, bit in enumerate(bits):
            gamma_map[idx][bit] += 1
    return gamma_map


def solution_part1(report):
    gamma_map = get_gamma_map(report)
    gamma = get_gamma(gamma_map)
    epsilon = get_epsilon(gamma)
    return int(gamma, 2) * int(epsilon, 2)


def get_bits_with_criteria(data, common_bit, bit_idx):
    results = []
    for bits in data:
        if bits[bit_idx] == common_bit:
            results.append(bits)
    return results


def solution_part2(report):
    oxygen_rating, co2_rating = list(report), list(report)
    current_bit_idx = 0
    bits_per_report = len(report[0])
    while len(oxygen_rating) != 1:
        oxygen_map = get_gamma_map(oxygen_rating)

        oxygen_zeroes = oxygen_map[current_bit_idx]['0']
        oxygen_ones = oxygen_map[current_bit_idx]['1']
        common_bit = '0' if oxygen_zeroes > oxygen_ones else '1'

        oxygen_rating = get_bits_with_criteria(oxygen_rating, common_bit, current_bit_idx)
        current_bit_idx = current_bit_idx + 1 % bits_per_report

    current_bit_idx = 0
    while len(co2_rating) != 1:
        co2_map = get_gamma_map(co2_rating)

        co2_zeroes = co2_map[current_bit_idx]['0']
        co2_ones = co2_map[current_bit_idx]['1']
        least_bit = '1' if co2_ones < co2_zeroes else '0'

        co2_rating = get_bits_with_criteria(co2_rating, least_bit, current_bit_idx)

        current_bit_idx = current_bit_idx + 1 % bits_per_report
    return int(oxygen_rating[0], 2) * int(co2_rating[0], 2)


if __name__ == '__main__':
    input_path = os.path.join(os.path.dirname(__file__), 'input.txt')
    with open(input_path, 'r') as f:
        diagnostic = [i.strip() for i in f.readlines()]
        print(solution_part1(diagnostic))
        print(solution_part2(diagnostic))
