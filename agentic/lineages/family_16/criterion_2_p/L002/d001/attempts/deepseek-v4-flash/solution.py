n = int(input())
ships = []
for _ in range(n):
    a, b = map(int, input().split())
    ships.append((a, b))

# Sort by lower lock time descending
ships.sort(key=lambda x: x[1], reverse=True)

upper_time = 0
lower_time = 0
for a, b in ships:
    upper_time += a
    lower_time = max(lower_time, upper_time) + b

print(lower_time)