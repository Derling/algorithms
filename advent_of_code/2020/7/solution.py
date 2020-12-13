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


def search1(bags: BagRulesMap, color: str) -> int:
    container_bags = set()
    for bag in bags:
        if color in bags[bag]:
            container_bags.add(bag)
            container_bags.update(search1(bags, bag))
    return container_bags


def search2(bags: BagRulesMap, color: str) -> int:
    count = 1
    for bag in bags[color]:
        multiplier = bags[color][bag]
        count += multiplier * search2(bags, bag)
    return count

def solution(bag_rules: List[str], search_func: callable) -> int:
    rules = get_rules_map(bag_rules)
    search_results = search_func(rules, 'shiny gold')
    # subtract 1 from search2 to exclude the base bag itself
    return search_results - 1 if search_func == search2 else len(search_results)


if __name__ == '__main__':
    import os
    fpath = os.path.join(os.path.dirname(__file__), 'input.txt')

    with open(fpath) as f:
        input_list = f.readlines()
        result = solution(input_list, search1)
        print(f'part 1 answer is {result}')

        print(solution(input_list, search2))