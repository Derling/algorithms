import os


def solution(sonar_pings):
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
        print(solution(pings))
