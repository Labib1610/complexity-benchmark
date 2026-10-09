from collections import defaultdict

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    k = int(data[0])
    t = int(data[1])
    
    if t < k:
        print("NO")
        return
    
    index = 2
    states = []
    pa_map = {}  # Maps p to its corresponding a
    ap_map = {}  # Maps a to its corresponding p
    
    for _ in range(t):
        p = int(data[index])
        a = int(data[index+1])
        m = int(data[index+2])
        states.append((p, a, m))
        index += 3
        
        if p in pa_map:
            if pa_map[p] != a:
                # This shouldn't happen according to problem statement
                print("NO")
                return
        else:
            pa_map[p] = a
            
        if a in ap_map:
            if ap_map[a] != p:
                # This shouldn't happen according to problem statement
                print("NO")
                return
        else:
            ap_map[a] = p
    
    # Group states by p (and equivalently by a)
    # For each p, we have a unique a, and a list of possible m values
    groups = defaultdict(list)
    for p, a, m in states:
        groups[p].append(m)
    
    # We need to find a perfect matching where for each p from 1 to k,
    # we select one state (p, a, m) such that all m values are distinct and cover 1 to k
    
    # This is equivalent to finding a perfect matching in a bipartite graph
    # Left side: principal numbers 1 to k
    # Right side: magnetic numbers 1 to k
    # Edge exists between p and m if there's a state with (p, a, m) 
    
    # Build adjacency list for matching
    adj = defaultdict(list)
    for p in range(1, k+1):
        if p not in groups:
            print("NO")
            return
        for m in groups[p]:
            adj[p].append(m)
    
    # Now we need to find a maximum matching that matches all k left nodes
    # This is the assignment problem - can be solved with Hungarian algorithm or DFS matching
    
    match_m_to_p = {}  # matching from magnetic number to principal number
    match_p_to_m = {}  # matching from principal number to magnetic number
    
    def dfs(p, visited):
        for m in adj[p]:
            if m in visited:
                continue
            visited.add(m)
            
            # If m is unmatched or we can find augmenting path
            if m not in match_m_to_p or dfs(match_m_to_p[m], visited):
                match_m_to_p[m] = p
                match_p_to_m[p] = m
                return True
        return False
    
    matched = 0
    for p in range(1, k+1):
        if p not in adj:
            print("NO")
            return
        visited = set()
        if dfs(p, visited):
            matched += 1
    
    if matched == k:
        print("YES")
        for p in range(1, k+1):
            m = match_p_to_m[p]
            a = pa_map[p]
            print(p, a, m)
    else:
        print("NO")

solve()