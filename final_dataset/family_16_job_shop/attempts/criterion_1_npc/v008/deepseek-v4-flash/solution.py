j, m = map(int, input().split())
jobs = []
for _ in range(j):
    data = list(map(int, input().split()))
    o = data[0]
    ops = [(data[i], data[i+1]) for i in range(1, 2*o, 2)]
    jobs.append(ops)

machine_free = [0] * (m + 1)  # 1-indexed machines
max_time = 0

for ops in jobs:
    current_time = 0
    for machine, duration in ops:
        current_time = max(current_time, machine_free[machine])
        current_time += duration
        machine_free[machine] = current_time
    max_time = max(max_time, current_time)

print(max_time)