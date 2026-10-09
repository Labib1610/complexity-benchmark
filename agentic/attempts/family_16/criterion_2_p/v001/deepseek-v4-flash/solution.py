n = int(input())
jobs = [tuple(map(int, input().split())) for _ in range(n)]

set1 = [job for job in jobs if job[0] <= job[1]]
set2 = [job for job in jobs if job[0] > job[1]]

set1.sort(key=lambda x: x[0])
set2.sort(key=lambda x: -x[1])

order = set1 + set2

time_a = 0
time_b = 0
for a, b in order:
    time_a += a
    time_b = max(time_a, time_b) + b

print(time_b)