from typing import List

def change_next_jpm_or_nop(commands: List[str], ignores: int) -> List[str]:
    new_commands = list(commands)
    ignored_changes = 0
    for i in range(len(new_commands)):
        current_op = new_commands[i]

        if make_nop := 'jmp' in current_op or 'nop' in current_op:

            if ignored_changes < ignores:
                ignored_changes += 1
                continue

            new_commands[i] = current_op.replace('jmp', 'nop') if make_nop else current_op.replace('nop', 'jmp')
            break
    
    return new_commands




def solution2(commands: List[str]) -> int:
    accumulator, is_infinite = solution(commands)
    ignore_changes = 0
    while is_infinite:
        new_commands = change_next_jpm_or_nop(commands, ignore_changes)
        accumulator, is_infinite = solution(new_commands)
        ignore_changes += 1
    return accumulator
        



def solution(commands: List[str]) -> int:
    accumulator = 0
    operations = set()
    current_op = 0
    while current_op < len(commands):
        op, acc_add = commands[current_op].split()
        next_op = 1

        if op == 'nop':
            acc_add = 0
        elif op == 'acc':
            acc_add = int(acc_add)
        else:
             next_op = int(acc_add)
             acc_add = 0

        if current_op + next_op in operations:
            return accumulator, True

        accumulator += acc_add
        operations.add(current_op)
        current_op += next_op

    return accumulator, False



if __name__ == '__main__':
    import os
    fpath = os.path.join(os.path.dirname(__file__), 'input.txt')

    with open(fpath) as f:
        input_list = [line.strip() for line in f.readlines()]
        result = solution(input_list)[0]
        print(f'part 1 answer is {result}')

        result = solution2(input_list)
        print(f'part 2 answer is {result}')
