from typing import List

word = "MAS"

table = ""
with open('./input.txt') as f:
    table = f.readlines()


a_poses = {}


def find_br_diag(i, j):
    row = table[i]
    if j >= 0 and j < len(row) and i >= 0 and i <= len(table) and j+len(word)-1 < len(row) and i+len(word)-1 < len(table):
        for (idx, char) in enumerate(word):
            if char != table[i+idx][j+idx]:
                return 0
        a_poses[(i+1, j+1)] = a_poses.get((i+1, j+1), 0) + 1
        return 1
    return 0


def find_tr_diag(i, j):
    row = table[i]
    if j >= 0 and j < len(row) and i >= 0 and i <= len(table) and j+len(word)-1 < len(row) and i-len(word)+1 >= 0:
        for (idx, char) in enumerate(word):
            if char != table[i-idx][j+idx]:
                return 0
        a_poses[(i-1, j+1)] = a_poses.get((i-1, j+1), 0) + 1
        return 1
    return 0


def find_tl_diag(i, j):
    row = table[i]
    if j >= 0 and j < len(row) and i >= 0 and i <= len(table) and j-len(word)+1 >= 0 and i-len(word)+1 >= 0:
        for (idx, char) in enumerate(word):
            if char != table[i-idx][j-idx]:
                return 0
        a_poses[(i-1, j-1)] = a_poses.get((i-1, j-1), 0) + 1
        return 1
    return 0


def find_bl_diag(i, j):
    row = table[i]
    if j >= 0 and j < len(row) and i >= 0 and i <= len(table) and j-len(word)+1 >= 0 and i+len(word)-1 < len(table):
        for (idx, char) in enumerate(word):
            if char != table[i+idx][j-idx]:
                return 0
        a_poses[(i+1, j-1)] = a_poses.get((i+1, j-1), 0) + 1
        return 1
    return 0


total = 0
for (i, row) in enumerate(table):
    for (j, col) in enumerate(row):
        if col == word[0]:
            br_diagonal = find_br_diag(i, j)
            tr_diagonal = find_tr_diag(i, j)
            tl_diagonal = find_tl_diag(i, j)
            bl_diagonal = find_bl_diag(i, j)

for key in a_poses:
    if a_poses[key] >= 2:
        total += a_poses[key] // 2

print(total)
