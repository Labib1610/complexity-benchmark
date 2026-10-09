from itertools import combinations

def main():
    n, m, k = map(int, input().split())
    
    # Read edges and build adjacency set for quick lookup
    edges = set()
    for _ in range(m):
        u, v = map(int, input().split())
        edges.add((u, v))
        edges.add((v, u))
    
    # Generate all combinations of k users
    users = list(range(1, n + 1))
    for combo in combinations(users, k):
        # Check if this combination forms an all-strangers group
        valid = True
        for i in range(k):
            for j in range(i + 1, k):
                u, v = combo[i], combo[j]
                if (u, v) in edges:
                    valid = False
                    break
            if not valid:
                break
        
        if valid:
            print("YES")
            print(" ".join(map(str, combo)))
            return
    
    print("NO")

if __name__ == "__main__":
    main()