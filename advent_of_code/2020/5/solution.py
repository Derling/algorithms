from typing import List, Mapping, Tuple, Union

TRAVERSAL_CONFIGS = {
    'row': {
        'range': (0, 128),
        'keys': ('F', 'B')
    },
    'col': {
        'range': (0, 8),
        'keys': ('L', 'R')
    }
}
PartitionMapping = Mapping[str, Mapping[str, Union[Tuple[int, int], Tuple[str, str]]]]


def traverse_partition_map(partition_str: str, partition_mapping: PartitionMapping) -> int:
    partition_min, partition_max = partition_mapping['range']
    min_key, _ = partition_mapping['keys']  # if its not one its the other

    for key in partition_str:
        partition_diff = partition_max - partition_min
        if key == min_key:
            partition_min, partition_max = partition_min, partition_max - (partition_diff // 2)
        else:
            partition_min, partition_max = partition_min + (partition_diff // 2), partition_max

    return partition_min if partition_str[-1] == min_key else partition_max - 1


def traverse_seat_map(seat_map: str, ) -> int:
    row_str, col_str = seat_map[:7], seat_map[7:]
    row = traverse_partition_map(row_str, TRAVERSAL_CONFIGS['row'])
    col = traverse_partition_map(col_str, TRAVERSAL_CONFIGS['col'])
    return row * 8 + col


def solution(seat_designations: List[str]) -> int:
    seat_ids = []
    for seat_designation in seat_designations:
        seat_ids.append(traverse_seat_map(seat_designation))
    return max(seat_ids)


if __name__ == '__main__':
    import os
    fpath = os.path.join(os.path.dirname(__file__), 'input.txt')

    with open(fpath) as f:
        input_list = f.readlines()
        result = solution(input_list)
        print(f'part 1 answer is {result}')