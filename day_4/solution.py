from typing import List

word = "XMAS"

table = ""
with open('./input.txt') as f:
    table = f.readlines()


def find_forward(i, j):
    row = table[i]
    if j >= 0 and j < len(row) and j+len(word)-1 < len(row):
        for (idx, char) in enumerate(word):
            if char != row[j+idx]:
                return 0
        return 1
    return 0


def find_backward(i, j):
    row = table[i]
    if j >= 0 and j < len(row) and j-len(word)+1 >= 0:
        for (idx, char) in enumerate(word):
            if char != row[j-idx]:
                return 0
        return 1
    return 0


def find_down(i, j):
    col = [row[j] for row in table]
    print(f"{i, j}: {i+len(word)-1}")
    if i >= 0 and i < len(col) and i+len(word)-1 < len(col):
        for (idx, char) in enumerate(word):
            if char != col[i+idx]:
                return 0
        return 1
    return 0


def find_up(i, j):
    col = [row[j] for row in table]
    print(f"{i, j}: {i-len(word)+1}")
    if i >= 0 and i < len(col) and i-len(word)+1 >= 0:
        for (idx, char) in enumerate(word):
            if char != col[i-idx]:
                return 0
        return 1
    return 0


def find_br_diag(i, j):
    row = table[i]
    if j >= 0 and j < len(row) and i >= 0 and i <= len(table) and j+len(word)-1 < len(row) and i+len(word)-1 < len(table):
        for (idx, char) in enumerate(word):
            if char != table[i+idx][j+idx]:
                return 0
        return 1
    return 0


def find_tr_diag(i, j):
    row = table[i]
    if j >= 0 and j < len(row) and i >= 0 and i <= len(table) and j+len(word)-1 < len(row) and i-len(word)+1 >= 0:
        for (idx, char) in enumerate(word):
            if char != table[i-idx][j+idx]:
                return 0
        return 1
    return 0


def find_tl_diag(i, j):
    row = table[i]
    if j >= 0 and j < len(row) and i >= 0 and i <= len(table) and j-len(word)+1 >= 0 and i-len(word)+1 >= 0:
        for (idx, char) in enumerate(word):
            if char != table[i-idx][j-idx]:
                return 0
        return 1
    return 0


def find_bl_diag(i, j):
    row = table[i]
    if j >= 0 and j < len(row) and i >= 0 and i <= len(table) and j-len(word)+1 >= 0 and i+len(word)-1 < len(table):
        for (idx, char) in enumerate(word):
            if char != table[i+idx][j-idx]:
                return 0
        return 1
    return 0


total = 0
for (i, row) in enumerate(table):
    for (j, col) in enumerate(row):
        if col == word[0]:
            forward = find_forward(i, j)
            backward = find_backward(i, j)
            downward = find_down(i, j)
            upward = find_up(i, j)
            br_diagonal = find_br_diag(i, j)
            tr_diagonal = find_tr_diag(i, j)
            tl_diagonal = find_tl_diag(i, j)
            bl_diagonal = find_bl_diag(i, j)
            total += forward + backward + downward + upward + \
                br_diagonal + tr_diagonal + tl_diagonal + bl_diagonal


print(total)
