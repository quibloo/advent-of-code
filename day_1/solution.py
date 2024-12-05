# Get lists from file
list1 = []
list2 = []
with open("./input.txt") as file:
    for line in file.readlines():
        l, r = line.split("   ")
        list1.append(int(l))
        list2.append(int(r))

sorted_l = sorted(list1)
sorted_r = sorted(list2)

total_dist = 0
dists = []
for i in range(len(sorted_l)):
    dist = abs(sorted_l[i] - sorted_r[i])
    print(f"Dist({sorted_l[i]},{sorted_r[i]}): {dist}")
    dists.append(dist)

for dist in dists:
    total_dist += dist

print(total_dist)
