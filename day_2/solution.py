from typing import List
# grab garbo from txt file
reports = []
with open("./input.txt") as f:
    for line in f.readlines():
        levels = []
        for level in line.split(" "):
            levels.append(int(level))
        reports.append(levels)


def get_diffs(report: List[int]):
    diffs = []
    prev = None
    is_increasing = False
    for level in report:
        if prev is None:
            prev = level
            continue
        diff = level - prev
        diffs.append(diff)
        prev = level
    return diffs


def check_inc(diffs: List[int]):
    for diff in diffs:
        if diff <= 0:
            return False
    return True


def check_dec(diffs: List[int]):
    for diff in diffs:
        if diff >= 0:
            return False
    return True


def check_range(diffs: List[int]):
    for diff in diffs:
        if 1 <= abs(diff) <= 3:
            continue
        else:
            return False
    return True


def gen_report_permutations(report: List[int]) -> List[List[int]]:
    perms = []
    for i in range(len(report)):
        new_report = report.copy()
        new_report.pop(i)
        perms.append(new_report)
    return perms


count = 0
for report in reports:
    perms = gen_report_permutations(report)
    any_safe = False
    for perm in perms:
        diffs = get_diffs(perm)
        inc = check_inc(diffs)
        dec = check_dec(diffs)
        in_range = check_range(diffs)
        is_safe = (inc or dec) and in_range
        any_safe = any_safe or is_safe
    if any_safe:
        count += 1

    print(f"Report: {report} {'Safe' if any_safe else 'Unsafe'}")
    print(f"Num safe: {count}")
