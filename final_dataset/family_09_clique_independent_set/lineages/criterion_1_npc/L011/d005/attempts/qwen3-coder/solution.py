from itertools import combinations

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    k = int(data[2])
    
    edges = []
    degree = [0] * (n + 1)
    
    idx = 3
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx + 1])
        idx += 2
        edges.append((u, v))
        degree[u] += 1
        degree[v] += 1
    
    ECL_base = 5 * m
    W_sum = sum(degree[i] for i in range(1, n + 1))
    
    # We need to check all combinations of k nodes
    # But n up to 46 makes C(n,k) too large.
    # However, given time limit 5s, we might be able to do it for small k or large k.
    # Let's try optimized approach: iterate over subsets of size k if k <= n/2,
    # otherwise iterate over subsets of size n-k and take complement.
    
    if k > n:
        print("NO")
        return
        
    nodes = list(range(1, n + 1))
    
    # Choose the smaller side to iterate
    if k <= n - k:
        iterate_k = k
        complement_flag = False
    else:
        iterate_k = n - k
        complement_flag = True
    
    from itertools import combinations
    
    # Precompute edge set for fast lookup
    edge_set = set((min(u,v), max(u,v)) for u,v in edges)
    
    for subset_tuple in combinations(nodes, iterate_k):
        subset = set(subset_tuple)
        if not complement_flag:
            panel = subset
            control = set(nodes) - panel
        else:
            control = subset
            panel = set(nodes) - control
            
        if len(panel) != k:
            continue
            
        sum_W_panel = sum(degree[i] for i in panel)
        sum_W_control = W_sum - sum_W_panel
        
        ECL = ECL_base + 2 * sum_W_panel + 3 * sum_W_control
        
        acl = 0
        for u, v in edges:
            if (u in panel and v in control) or (u in control and v in panel):
                acl += 10
            elif u in panel and v in panel:
                acl += 5
            else:  # both in control
                acl += 11
                
        if acl == ECL:
            print("YES")
            print(' '.join(map(str, sorted(panel))))
            return
            
    print("NO")

if __name__ == "__main__":
    main()