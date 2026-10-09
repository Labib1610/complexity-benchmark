from itertools import combinations

def solve():
    k, t = map(int, input().split())
    
    if t < k:
        print("NO")
        return
    
    models = []
    for _ in range(t):
        a, b, c = map(int, input().split())
        models.append((a, b, c))
    
    # Try all combinations of k models
    for combo in combinations(models, k):
        # Count unique values for each parameter
        alpha_vals = set(model[0] for model in combo)
        beta_vals = set(model[1] for model in combo)
        gamma_vals = set(model[2] for model in combo)
        
        # Calculate resonance score
        score = len(alpha_vals) + len(beta_vals) + len(gamma_vals)
        
        # Check if score equals 3k
        if score == 3 * k:
            print("YES")
            for model in combo:
                print(model[0], model[1], model[2])
            return
    
    print("NO")

solve()