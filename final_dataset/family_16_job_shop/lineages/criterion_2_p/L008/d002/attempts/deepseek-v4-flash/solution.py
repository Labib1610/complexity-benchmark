n = int(input())
jobs = []
for _ in range(n):
    p1, p2 = map(int, input().split())
    jobs.append((p1, p2))

# Johnson's rule
A = []
B = []
for p1, p2 in jobs:
    if p1 <= p2:
        A.append((p1, p2))
    else:
        B.append((p1, p2))

A.sort(key=lambda x: x[0])  # sort by p1 ascending
B.sort(key=lambda x: x[1], reverse=True)  # sort by p2 descending

order = A + B

# Simulate
time_radar = 0
time_sampling = 0
for p1, p2 in order:
    time_radar += p1
    if time_sampling < time_radar:
        time_sampling = time_radar
    time_sampling += p2

print(time_sampling)