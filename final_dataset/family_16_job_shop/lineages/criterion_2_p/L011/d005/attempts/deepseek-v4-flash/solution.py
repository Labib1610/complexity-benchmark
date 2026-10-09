j = int(input())
jobs = []
for _ in range(j):
    a, b = map(int, input().split())
    jobs.append((a, b))

# Johnson's rule sorting
first = []
second = []
for a, b in jobs:
    if a < b:
        first.append((a, b))
    else:
        second.append((a, b))

first.sort(key=lambda x: x[0])          # sort by p1 ascending
second.sort(key=lambda x: -x[1])        # sort by p2 descending

order = first + second

time_a = 0
time_b = 0
for a, b in order:
    time_a += a
    if time_b < time_a:
        time_b = time_a
    time_b += b

print(time_b)