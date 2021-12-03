import os


def solution_part2(sonar_pings, sliding_window):
    increases = 0
    current_sum = sum(sonar_pings[:sliding_window])

    for i in range(sliding_window, len(sonar_pings)):
        next_sum = sum(sonar_pings[i - (sliding_window - 1): i + 1])
        if next_sum > current_sum:
            increases += 1
        current_sum = next_sum

    return increases


def solution_part1(sonar_pings):
    current_ping = sonar_pings[0]
    increases = 0

    for ping in sonar_pings[1:]:
        if ping > current_ping:
            increases += 1
        current_ping = ping

    return increases


if __name__ == '__main__':
    input_path = os.path.join(os.path.dirname(__file__), 'input.txt')
    with open(input_path, 'r') as f:
        pings = [int(i) for i in f.read().splitlines()]
        print(solution_part1(pings))
        print(solution_part2(pings, 3))
