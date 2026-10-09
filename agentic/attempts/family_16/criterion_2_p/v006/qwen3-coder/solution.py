j = int(input())
containers = []
for _ in range(j):
    p1, p2 = map(int, input().split())
    containers.append((p1, p2))

# Sort by inspection time ascending, then by loading time descending
# This is a variant of Johnson's rule for two-machine flow shop scheduling
containers.sort(key=lambda x: (x[0], -x[1]))

# Simulate the process
inspection_finish_time = 0
loading_start_time = 0

for p1, p2 in containers:
    inspection_finish_time += p1
    loading_start_time = max(loading_start_time, inspection_finish_time)
    loading_start_time += p2

print(loading_start_time)