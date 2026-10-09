n = int(input())
jobs = [tuple(map(int, input().split())) for _ in range(n)]

# Johnson's rule
first = []
second = []
for p1, p2 in jobs:
    if p1 < p2:
        first.append((p1, p2))
    else:
        second.append((p1, p2))

first.sort(key=lambda x: x[0])          # ascending by compression time
second.sort(key=lambda x: x[1], reverse=True)  # descending by encryption time

schedule = first + second

comp_time = 0
enc_time = 0
for p1, p2 in schedule:
    comp_time += p1
    enc_time = max(enc_time, comp_time) + p2

print(enc_time)