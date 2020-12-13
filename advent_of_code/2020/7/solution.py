from collections import defaultdict
from typing import List, Mapping


BagRulesMap = Mapping[str, Mapping[str, int]]


def get_rules_map(bag_rules: List[str]) -> BagRulesMap:
    bags = defaultdict(dict)
    for rule in bag_rules:
        bag, inner_bags = rule.split(' bags contain ')
        inner_bags = [i.split(' bag')[0].strip() for i in inner_bags.split(',')]
        for inner_bag in inner_bags:
            if inner_bag == 'no other':
                bags[bag] = {}
            else:
                count, name = int(inner_bag[0]), inner_bag[2:]
                bags[bag][name] = count
    return bags


def search(bags: BagRulesMap, color: str) -> int:
    container_bags = set()
    for bag in bags:
        if color in bags[bag]:
            container_bags.add(bag)
            container_bags.update(search(bags, bag))
    return container_bags

def solution(bag_rules: List[str]) -> int:
    rules = get_rules_map(bag_rules)
    container_bags = search(rules, 'shiny gold')
    return len(container_bags)


if __name__ == '__main__':
    import os
    fpath = os.path.join(os.path.dirname(__file__), 'input.txt')

    with open(fpath) as f:
        input_list = f.readlines()
        result = solution(input_list)
        print(f'part 1 answer is {result}')
