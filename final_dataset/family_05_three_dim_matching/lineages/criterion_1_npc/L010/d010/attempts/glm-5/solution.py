import sys
from itertools import permutations

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    idx = 0
    k = int(input_data[idx]); idx += 1
    t = int(input_data[idx]); idx += 1
    relays = []
    for _ in range(t):
        a = int(input_data[idx]); idx += 1
        b = int(input_data[idx]); idx += 1
        c = int(input_data[idx]); idx += 1
        relays.append((a, b, c))
    
    if k == 0:
        print("YES")
        return
    
    # Group relays by their 'a' value
    by_a = [[] for _ in range(k + 1)]
    for i, (a, b, c) in enumerate(relays):
        by_a[a].append(i)
    
    # Check if any a-value has no relays
    for v in range(1, k + 1):
        if not by_a[v]:
            print("NO")
            return
    
    # Bipartite matching with augmenting paths
    def can_match(adj, n_left, n_right):
        match_r = [-1] * (n_right + 1)
        def try_kuhn(v, visited):
            for u in adj[v]:
                if not visited[u]:
                    visited[u] = True
                    if match_r[u] == -1 or try_kuhn(match_r[u], visited):
                        match_r[u] = v
                        return True
            return False
        for v in range(1, n_left + 1):
            visited = [False] * (n_right + 1)
            if not try_kuhn(v, visited):
                return None
        return match_r
    
    # Try all permutations of which relay is assigned to each a-value
    # For each, check if b and c channels can also form perfect matchings
    for perm in permutations(range(k)):
        # perm[i] = index into by_a[i+1] of the relay assigned a-value (i+1)
        selected = []
        valid = True
        for i in range(k):
            lst = by_a[i + 1]
            if perm[i] >= len(lst):
                valid = False
                break
            selected.append(relays[lst[perm[i]]])
        if not valid:
            continue
        
        # Check b-channel matching
        adj_b = [[] for _ in range(k + 1)]
        for i in range(k):
            adj_b[i + 1].append(selected[i][1])
        if can_match(adj_b, k, k) is None:
            continue
        
        # Check c-channel matching
        adj_c = [[] for _ in range(k + 1)]
        for i in range(k):
            adj_c[i + 1].append(selected[i][2])
        if can_match(adj_c, k, k) is None:
            continue
        
        print("YES")
        for (a, b, c) in selected:
            print(a, b, c)
        return
    
    print("NO")

solve()