n = int(input())
requests = [tuple(map(int, input().split())) for _ in range(n)]

# Sort by Phase A time
requests.sort(key=lambda x: x[0])

time_a = 0
time_b = 0

for a, b in requests:
    time_a += a
    time_b = max(time_b, time_a) + b

print(time_b)