def solve():
    n, b = map(int, input().split())
    investments = []
    for _ in range(n):
        cost, value = map(int, input().split())
        investments.append((cost, value))
    
    investments.sort(key=lambda x: x[1] / x[0], reverse=True)
    
    total_value = 0.0
    remaining_budget = b
    
    for cost, value in investments:
        if cost <= remaining_budget:
            total_value += value
            remaining_budget -= cost
        else:
            fraction = remaining_budget / cost
            total_value += fraction * value
            remaining_budget = 0
            break
    
    print(f"{total_value:.6f}")

solve()