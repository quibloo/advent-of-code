from typing import List
import re
# okay so it kinda looks like we just need to search for "mul"
# then check for matching open closed parens
# then read the numbers inside the parens
# then multiply them
# then add 'em all up!


def fetch_src():
    src = ""
    with open("./input.corrupt") as f:
        src = str(f.readlines())
    return src


def find_ops(src: str):
    match = re.findall(r'mul\([0-9]*,[0-9]*\)|don\'t\(\)|do\(\)', src)
    return match


def parse_and_exec_mul(op: str):
    x, y = str(re.search(r'[0-9]*,[0-9]*', op).group()).split(",")
    print(f"x:{x}, y:{y}")
    return int(x) * int(y)


def main():
    src = fetch_src()
    ops = find_ops(src)
    total = 0
    enabled = True
    for op in ops:
        if re.search(r'mul\([0-9]*,[0-9]*\)', op) is not None:
            product = parse_and_exec_mul(op)
            if enabled:
                total += product
        elif re.search(r'don\'t\(\)', op) is not None:
            enabled = False
        elif re.search(r'do\(\)', op) is not None:
            enabled = True
    print(total)


main()
