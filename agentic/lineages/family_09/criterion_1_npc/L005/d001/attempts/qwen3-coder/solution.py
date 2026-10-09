from itertools import combinations

def main():
    n, m, k = map(int, input().split())
    
    # Create adjacency list to store grievances
    # If u has a grievance against v, we store v in adj[u]
    adj = [set() for _ in range(n + 1)]
    
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].add(v)
    
    # Generate all possible combinations of k employees
    for combo in combinations(range(1, n + 1), k):
        # Check if this combination is harmonious
        is_harmonious = True
        for i in range(k):
            for j in range(k):
                if i != j:
                    # If employee combo[i] has a grievance against combo[j]
                    if combo[j] in adj[combo[i]]:
                        is_harmonious = False
                        break
            if not is_harmonious:
                break
        
        if is_harmonious:
            print("YES")
            print(*combo)
            return
    
    print("NO")

if __name__ == "__main__":
    main()