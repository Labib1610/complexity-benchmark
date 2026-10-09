from itertools import combinations
import sys

def main():
    n, m, k = map(int, sys.stdin.readline().split())
    
    # Create adjacency list
    adj = [set() for _ in range(n + 1)]
    
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].add(v)
        adj[v].add(u)
    
    # Generate all combinations of k users
    for combo in combinations(range(1, n + 1), k):
        # Check if this combination is unacquainted
        valid = True
        for i in range(k):
            for j in range(i + 1, k):
                if combo[j] in adj[combo[i]]:
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