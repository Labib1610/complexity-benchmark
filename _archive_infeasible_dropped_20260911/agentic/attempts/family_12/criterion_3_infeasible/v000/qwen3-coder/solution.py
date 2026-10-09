n, B = map(int, input().split())
min_cost = float('inf')
for _ in range(n):
    cost, value = map(int, input().split())
    min_cost = min(min_cost, cost)
print(f"MIN {min_cost}")