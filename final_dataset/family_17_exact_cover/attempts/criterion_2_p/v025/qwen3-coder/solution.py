from collections import defaultdict, deque

def solve():
    q, t = map(int, input().split())
    
    # Build adjacency list for cores to dissipators
    adj = defaultdict(list)
    for _ in range(t):
        a, b = map(int, input().split())
        adj[a].append(b)
    
    # Try to find a maximum matching using BFS-based approach (Hopcroft-Karp like)
    # But we'll use a simpler approach: try to find a matching using DFS
    
    # pair_core[c] = d means core c is matched to dissipator d
    # pair_diss[d] = c means dissipator d is matched to core c
    pair_core = [0] * (q + 1)  # 1-indexed
    pair_diss = [0] * (2 * q + 1)  # 1-indexed
    
    def dfs(core, visited):
        for diss in adj[core]:
            if visited[diss]:
                continue
            visited[diss] = True
            
            # If dissipator is free or we can find an augmenting path
            if pair_diss[diss] == 0 or dfs(pair_diss[diss], visited):
                pair_core[core] = diss
                pair_diss[diss] = core
                return True
        return False
    
    matched = 0
    for core in range(1, q + 1):
        visited = [False] * (2 * q + 1)
        if dfs(core, visited):
            matched += 1
    
    if matched == q:
        print("YES")
        for core in range(1, q + 1):
            print(core, pair_core[core])
    else:
        print("NO")

solve()