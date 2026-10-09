import sys
from collections import deque
from itertools import combinations

# Increase recursion depth just in case
sys.setrecursionlimit(300000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    M = int(input_data[1])
    T = int(input_data[2])
    m = int(input_data[3])
    
    adj = [[] for _ in range(n + 1)]
    in_degree = [0] * (n + 1)
    
    idx = 4
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        adj[u].append(v)
        in_degree[v] += 1
        idx += 2
        
    # Check total capacity
    if n > M * T:
        print("NO")
        return
        
    # Cycle detection and topological sort / height calculation
    # height[u]: length of longest path from u to any sink (in terms of number of nodes)
    # A sink has height 1.
    rev_adj = [[] for _ in range(n + 1)]
    out_degree = [0] * (n + 1)
    for u in range(1, n + 1):
        for v in adj[u]:
            rev_adj[v].append(u)
            out_degree[u] += 1
            
    # Kahn's algorithm from sinks backwards to compute height
    height = [1] * (n + 1)
    q = deque()
    for i in range(1, n + 1):
        if out_degree[i] == 0:
            q.append(i)
            
    visited_count = 0
    while q:
        u = q.popleft()
        visited_count += 1
        for p in rev_adj[u]:
            if height[u] + 1 > height[p]:
                height[p] = height[u] + 1
            out_degree[p] -= 1
            if out_degree[p] == 0:
                q.append(p)
                
    if visited_count < n:
        # Cycle detected
        print("NO")
        return
        
    # LST[u] = T - height[u] + 1
    lst = [T - height[u] + 1 for u in range(n + 1)]
    for u in range(1, n + 1):
        if lst[u] < 1:
            print("NO")
            return

    # Count of successors (transitive or direct) to break ties
    num_succ = [len(adj[u]) for u in range(n + 1)]
    
    assigned_minute = [0] * (n + 1)
    current_in_deg = list(in_degree)
    
    ready_jobs = [u for u in range(1, n + 1) if current_in_deg[u] == 0]
    
    def search(minute, rem_ready, remaining_jobs_count):
        if remaining_jobs_count == 0:
            return True
        if minute > T:
            return False
        
        # Pruning 1: Volume check
        if remaining_jobs_count > (T - minute + 1) * M:
            return False
            
        must = []
        optional = []
        
        for u in rem_ready:
            if lst[u] < minute:
                return False
            elif lst[u] == minute:
                must.append(u)
            else:
                optional.append(u)
                
        if len(must) > M:
            return False
            
        needed = min(M - len(must), len(optional))
        
        # Sort optional by heuristic: highest height first, then most successors
        optional.sort(key=lambda u: (-height[u], -num_succ[u]))
        
        # If all ready jobs fit in this minute
        if len(rem_ready) <= M:
            chosen_combinations = [tuple(optional)]
        else:
            # We need to choose `needed` jobs from `optional`
            # To avoid exploring too many branches, combinations are generated in heuristic order
            chosen_combinations = combinations(optional, needed)
            
        for opt_chosen in chosen_combinations:
            scheduled = must + list(opt_chosen)
            
            # Apply schedule
            for u in scheduled:
                assigned_minute[u] = minute
                
            new_ready = [u for u in rem_ready if assigned_minute[u] == 0]
            
            # Unlock successors
            for u in scheduled:
                for v in adj[u]:
                    current_in_deg[v] -= 1
                    if current_in_deg[v] == 0:
                        new_ready.append(v)
                        
            if search(minute + 1, new_ready, remaining_jobs_count - len(scheduled)):
                return True
                
            # Rollback
            for u in scheduled:
                assigned_minute[u] = 0
                for v in adj[u]:
                    current_in_deg[v] += 1

        return False

    if search(1, ready_jobs, n):
        print("YES")
        print(*(assigned_minute[1:]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()