# Get lists from file
list1 = []
list2 = []
with open("./input.txt") as file:
    for line in file.readlines():
        l, r = line.split("   ")
        list1.append(int(l))
        list2.append(int(r))

counts = {}

for el in list2:
    counts[el] = counts.get(el, 0) + 1

sim_score = 0
for el in list1:
    sim_score += el * counts.get(el, 0)

print(sim_score)
