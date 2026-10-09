from itertools import combinations

def solve():
    n, m, k = map(int, input().split())
    
    # Build adjacency list to store shared blocks
    adj = [[] for _ in range(n + 1)]
    edges = []
    
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))
    
    # For each possible combination of k documents
    for combo in combinations(range(1, n + 1), k):
        selected = set(combo)
        
        sum_ref_count = 0
        shared_blocks = set()
        
        # Calculate sum of reference counts and collect shared blocks
        for doc in selected:
            count = 0
            for neighbor in adj[doc]:
                if neighbor in selected:
                    count += 1
                    # Add the shared block (min, max) to avoid duplicates
                    shared_blocks.add((min(doc, neighbor), max(doc, neighbor)))
            sum_ref_count += count
        
        # The archive footprint is the number of unique shared blocks
        archive_footprint = len(shared_blocks)
        
        # Check if they are equal
        if sum_ref_count == archive_footprint:
            print("YES")
            print(*combo)
            return
    
    print("NO")

solve()