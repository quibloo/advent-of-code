from typing import List
import functools

rules = []
updates = []
with open("./input.txt") as f:
    is_rule = True
    for line in f.readlines():
        if line == "\n":
            is_rule = False
            continue
        if is_rule:
            rules.append(line.replace("\n", ""))
        else:
            updates.append(line.replace("\n", ""))


def parse_rule(rule: str):
    page_1 = ""
    page_2 = ""
    separator_idx = len(rule)
    i = 0
    for i in range(len(rule)):
        if rule[i] == '|':
            separator_idx = i
        if i < separator_idx:
            page_1 += rule[i]
        elif i > separator_idx:
            page_2 += rule[i]

    return (int(page_1), int(page_2))


def build_rule_map(parsed_rules):
    rule_map = {}
    for before, after in parsed_rules:
        rule_map[before] = rule_map.get(before, []) + [after]
    return rule_map


rule_map = build_rule_map(map(parse_rule, rules))


def check_ordering_constraints(i, num, idx_map):
    for rule in rule_map.get(num, []):
        # if rule doesn't exist or rule is satisfied then continue
        if idx_map.get(rule) is None or i < idx_map.get(rule):
            continue
        # otherwise fail it
        else:
            return False
    return True


def parse_update(update: str):
    return list(map(int, update.split(",")))


def check_update(parsed_update: List[int]):
    idx_map = {}
    # build hash table of num indexes
    for i, num in enumerate(parsed_update):
        idx_map[num] = i

    # check constraint for each index
    for i, num in enumerate(parsed_update):
        if check_ordering_constraints(i, num, idx_map) is False:
            return False
    return True


def compare(x, y):
    if y in rule_map.get(x, []):
        return -1
    elif x in rule_map.get(y, []):
        return 1
    else:
        return 0


def correct_update(update: List[int]):
    idx_map = {}
    for i, num in enumerate(update):
        idx_map[num] = i
    return sorted(update, key=functools.cmp_to_key(compare))


total = 0
incorrect = []
for update in updates:
    parsed_update = parse_update(update)
    passed = check_update(parsed_update)
    if passed:
        total += parsed_update[len(parsed_update) // 2]
    else:
        incorrect.append(parsed_update)
    # print(f"{update}: {passed}")

incorrect_total = 0
for update in incorrect:
    corrected = correct_update(update)
    print(f"Corrected: {corrected}")
    incorrect_total += corrected[len(corrected)//2]


print(f"Total: {total}")
print(f"Incorrect Total: {incorrect_total}")
