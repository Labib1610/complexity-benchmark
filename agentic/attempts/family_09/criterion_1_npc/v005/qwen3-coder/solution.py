from itertools import combinations

def main():
    n, m, k = map(int, input().split())
    
    # Create adjacency list representation of the graph
    adj = [set() for _ in range(n + 1)]
    
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].add(v)
        adj[v].add(u)
    
    # Generate all combinations of k users
    users = list(range(1, n + 1))
    
    for combo in combinations(users, k):
        # Check if this combination forms an all-strangers group
        is_valid = True
        for i in range(k):
            for j in range(i + 1, k):
                u, v = combo[i], combo[j]
                if u in adj[v]:  # If they are friends, this combo is invalid
                    is_valid = False
                    break
            if not is_valid:
                break
        
        if is_valid:
            print("YES")
            print(" ".join(map(str, combo)))
            return
    
    print("NO")

if __name__ == "__main__":
    main()