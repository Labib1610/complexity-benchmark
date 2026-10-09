import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    it = iter(input_data)
    n = int(next(it))
    M = int(next(it))
    T = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(n + 1)]
    rev_adj = [[] for _ in range(n + 1)]
    in_degree = [0] * (n + 1)
    out_degree = [0] * (n + 1)
    
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        rev_adj[v].append(u)
        in_degree[v] += 1
        out_degree[u] += 1

    # Check for cycles and compute earliest possible room (1-based)
    q = deque([i for i in range(1, n + 1) if in_degree[i] == 0])
    earliest = [1] * (n + 1)
    topo_order = []
    
    in_deg_copy = list(in_degree)
    while q:
        u = q.popleft()
        topo_order.append(u)
        for v in adj[u]:
            if earliest[u] + 1 > earliest[v]:
                earliest[v] = earliest[u] + 1
            in_deg_copy[v] -= 1
            if in_deg_copy[v] == 0:
                q.append(v)
                
    if len(topo_order) < n:
        print("NO")
        return

    # Compute latest possible room
    latest = [T] * (n + 1)
    for u in reversed(topo_order):
        for v in adj[u]:
            if latest[v] - 1 < latest[u]:
                latest[u] = latest[v] - 1

    for i in range(1, n + 1):
        if earliest[i] > latest[i] or earliest[i] > T or latest[i] < 1:
            print("NO")
            return

    # Coffman-Graham labeling for tie-breaking / priority
    # Label from 1 to n
    # Transitive reduction could be used, but full successor labels sorted descending works well
    labels = [0] * (n + 1)
    out_deg_copy = list(out_degree)
    q_rev = [i for i in range(1, n + 1) if out_deg_copy[i] == 0]
    
    for label in range(1, n + 1):
        if not q_rev:
            break
        # Pick vertex whose sorted list of successor labels is lexicographically smallest
        best_u = -1
        best_key = None
        for u in q_rev:
            succ_labels = sorted([labels[v] for v in adj[u]], reverse=True)
            if best_key is None or succ_labels < best_key:
                best_key = succ_labels
                best_u = u
        
        labels[best_u] = label
        q_rev.remove(best_u)
        for p in rev_adj[best_u]:
            out_deg_copy[p] -= 1
            if out_deg_copy[p] == 0:
                q_rev.append(p)

    # Heuristic: priority by (latest deadline, -label)
    # Forward simulation / search
    room_assignment = [0] * (n + 1)
    
    # Backtracking search with branch-and-bound
    # To be extremely fast, we try list scheduling first (greedy)
    # If greedy fails, fall back to DFS.
    
    def try_list_scheduling():
        curr_in_deg = list(in_degree)
        room_of = [0] * (n + 1)
        ready = [[] for _ in range(T + 2)]
        
        for i in range(1, n + 1):
            if curr_in_deg[i] == 0:
                ready[earliest[i]].append(i)
                
        available = []
        for t in range(1, T + 1):
            for u in ready[t]:
                available.append(u)
            # Sort available by priority: smallest latest[u], then largest label
            available.sort(key=lambda u: (latest[u], -labels[u]))
            
            chosen = available[:M]
            available = available[M:]
            
            for u in chosen:
                room_of[u] = t
                for v in adj[u]:
                    curr_in_deg[v] -= 1
                    if curr_in_deg[v] == 0:
                        ready[max(t + 1, earliest[v])].append(v)
                        
        if all(room_of[i] > 0 for i in range(1, n + 1)):
            return room_of
        return None

    res = try_list_scheduling()
    if res:
        print("YES")
        print(*(res[1:]))
        return

    # DFS if greedy didn't succeed immediately
    assigned_count = 0
    room_of = [0] * (n + 1)
    curr_in_deg = list(in_degree)

    def dfs(t, available):
        nonlocal assigned_count
        if assigned_count == n:
            return True
        if t > T:
            return False
        
        # Check deadline feasibility
        for u in available:
            if latest[u] < t:
                return False

        # Generate subsets of size <= M to pick for room t
        # High-priority elements must be chosen if their latest == t
        must_pick = [u for u in available if latest[u] == t]
        if len(must_pick) > M:
            return False
            
        others = [u for u in available if latest[u] > t]
        others.sort(key=lambda u: (latest[u], -labels[u]))
        
        k = min(M - len(must_pick), len(others))
        
        # We try combinations of size up to M, greedily starting with the highest priority
        chosen_prefix = must_pick + others[:k]
        
        # Try full capacity first
        chosen_candidates = [chosen_prefix]
        
        for chosen in chosen_candidates:
            new_avail = [u for u in available if u not in chosen]
            for u in chosen:
                room_of[u] = t
                assigned_count += 1
            
            new_ready = []
            for u in chosen:
                for v in adj[u]:
                    curr_in_deg[v] -= 1
                    if curr_in_deg[v] == 0:
                        new_ready.append(v)
            
            next_available = new_avail + new_ready
            if dfs(t + 1, next_available):
                return True
            
            for u in chosen:
                for v in adj[u]:
                    curr_in_deg[v] += 1
                room_of[u] = 0
                assigned_count -= 1
                
        return False

    init_available = [i for i in range(1, n + 1) if in_degree[i] == 0]
    if dfs(1, init_available):
        print("YES")
        print(*(room_of[1:]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()