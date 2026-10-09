j = int(input())
trains = [tuple(map(int, input().split())) for _ in range(j)]

# Johnson's rule
group1 = []  # X < Y
group2 = []  # X >= Y

for x, y in trains:
    if x < y:
        group1.append((x, y))
    else:
        group2.append((x, y))

group1.sort(key=lambda t: t[0])       # increasing X
group2.sort(key=lambda t: -t[1])      # decreasing Y

order = group1 + group2

# Simulate
t_struct = 0
t_cargo = 0
for x, y in order:
    t_struct += x
    if t_cargo < t_struct:
        t_cargo = t_struct
    t_cargo += y

print(t_cargo)