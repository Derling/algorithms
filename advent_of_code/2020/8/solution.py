from typing import List

def solution(commands: List[str]) -> int:
    accumulator = 0
    operations = set()
    current_op = 0
    while True:
        op, acc_add = commands[current_op].split()
        next_op = 1

        print(current_op, op, acc_add, accumulator)
        if op == 'nop':
            acc_add = 0
        elif op == 'acc':
            acc_add = int(acc_add)
        else:
             next_op = int(acc_add)
             acc_add = 0

        if current_op + next_op in operations:
            break

        accumulator += acc_add
        operations.add(current_op)
        current_op += next_op

    return accumulator



if __name__ == '__main__':
    import os
    fpath = os.path.join(os.path.dirname(__file__), 'input.txt')

    with open(fpath) as f:
        input_list = [line.strip() for line in f.readlines()]
        result = solution(input_list)
        print(f'part 1 answer is {result}')
