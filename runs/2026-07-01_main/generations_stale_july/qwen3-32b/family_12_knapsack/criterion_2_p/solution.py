n, B = map(int, input().split())
investments = []
for _ in range(n):
    cost, value = map(int, input().split())
    investments.append((cost, value))

# Sort investments by value per cost in descending order
investments.sort(key=lambda x: (x[1]/x[0]), reverse=True)

remaining = B
total = 0.0

for cost, value in investments:
    if remaining <= 0:
        break
    take = min(remaining, cost)
    total += (take / cost) * value
    remaining -= take

print("{0:.6f}".format(total))